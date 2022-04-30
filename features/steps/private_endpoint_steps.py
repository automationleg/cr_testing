import time

from behave import step
from hamcrest import *
import json
from features.api_objects.private import UserData, Auth


@step('POST Request is sent to get "{endpoint_uri}" User Data')
def step_impl(context, endpoint_uri):
    # add optional payload params
    payload_data = json.loads(context.text) if context.text else {}

    auth = Auth(uri=endpoint_uri,
                api_key=context.api_key,
                api_secret=context.api_sec,
                payload_data=payload_data,
                )
    user_data = UserData(f"{context.site_base_url}", auth=auth, otp=context.api_otp)

    context.response = user_data.get_data(endpoint_uri, payload_data)


@step("The following orders were opened")
def step_impl(context):
    context.expected_open_orders = [dict(zip(row.headings, row.cells)) for row in context.table]


@step("There is {expected_opened:d} opened order found in response")
@step("There are {expected_opened:d} opened orders found in response")
def step_impl(context, expected_opened):
    opened_orders_count = len(context.response.json()['result']['open'].keys())
    assert_that(opened_orders_count, equal_to(expected_opened),
                'Number of opened orders is incorrect'
                )


@step('Opened orders with corresponding descr attributes are found in the response')
def step_impl(context):
    expected_open_orders = [dict(zip(row.headings, row.cells)) for row in context.table]
    actual_open_orders = context.response.json()['result']['open']

    # collect orders that have attributes different from expected
    incorrect_orders = []
    for expected_order in expected_open_orders:
        found_item = {}
        for k, v in actual_open_orders.items():
            if v['descr'] | expected_order == v['descr']:
                found_item = expected_order
                break
        if not found_item:
            incorrect_orders.append(expected_order)

    assert not incorrect_orders, \
        f'Open Orders with the following properties have not been found in the response: {incorrect_orders}'


@step("Opened orders with general order attributes are found in the response")
def step_impl(context):
    expected_order_attributes = [dict(zip(row.headings, row.cells)) for row in context.table]
    actual_order_attributes = context.response.json()['result']['open']

    # collect orders that have attributes different from expected
    incorrect_orders = []
    for expected_order in expected_order_attributes:
        found_item = {}
        for k, v in actual_order_attributes.items():
            if v | expected_order == v['descr']:
                found_item = expected_order
                break
        if not found_item:
            incorrect_orders.append(expected_order)

    assert not incorrect_orders, \
        f'Open Orders with the following properties have not been found in the response: {incorrect_orders}'
