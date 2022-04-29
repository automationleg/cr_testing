import json
import logging
from importlib import import_module

import requests as r
from behave import step
from hamcrest import *
from jsonpath_rw_ext import parse
from jsonschema import validate

from features import json_schemas


@step(u'Request is sent to "{uri}" URI')
def step_impl(context, uri):
    context.response = r.get(f'{context.site_base_url}{uri}')


@step('Response is "{http_code}"')
def step_impl(context, http_code):
    logging.info(f'Got response: {context.response.text}')
    assert_that(context.response.status_code, equal_to(int(http_code)),
                f'Unexpected response code.\n{context.response.text}'
                )


@step('Json response is matching the schema')
def step_impl(context):
    schema = json.loads(context.text)
    validate(context.response.json(), schema)


@step('Json response is matching the "{json_schema}" json schema from "{schema_file_name}" file')
def step_impl(context, json_schema, schema_file_name):
    json_schema_file = import_module(f'.{schema_file_name}', json_schemas.__name__)
    loaded_schema = json.loads(getattr(json_schema_file, json_schema))
    validate(context.response.json(), loaded_schema)


@step('Field "{field_path}" in response json is equal to "{value}"')
def step_impl(context, field_path, value):
    jsonpath_expression = parse(field_path)
    match = jsonpath_expression.find(context.response.json())

    assert_that(str(match[0].value), equal_to(value))


@step('Field "{field_path}" in response json contains "{text}" text')
def step_impl(context, field_path, text):
    jsonpath_expression = parse(field_path)
    match = jsonpath_expression.find(context.response.json())

    assert_that(str(match[0].value), contains_string(text))


@step('List Field "{field_path}" in response json contains the following values')
def step_impl(context, field_path):
    expected_values_in_list = [row['value'] for row in context.table]

    jsonpath_expression = parse(field_path)
    match = jsonpath_expression.find(context.response.json())

    assert_that(match[0].value, has_items(*expected_values_in_list))


@step('List Field "{field_path}" in response json contains the following integer values')
def step_impl(context, field_path):
    expected_values_in_list = [int(row['value']) for row in context.table]

    jsonpath_expression = parse(field_path)
    match = jsonpath_expression.find(context.response.json())

    assert_that([item.value for item in match], has_items(*expected_values_in_list))


@step('List Field "{field_path}" in response json contains the following fee value pairs')
def step_impl(context, field_path):
    expected_values_in_list = [[int(row['size']), float(row['fee'])] for row in context.table]

    jsonpath_expression = parse(field_path)
    match = jsonpath_expression.find(context.response.json())

    assert_that([item.value for item in match], has_items(*expected_values_in_list))


@step('Json response is equal to')
def step_impl(context):
    expected_response = json.loads(context.text)
    assert_that(
        context.response.json(),
        equal_to(expected_response),
        'Received response is incorrect',
    )


@step('Http response contains "{text}"')
def step_impl(context, text):
    assert_that(
        context.response.text,
        contains_string(text),
        'Received http response is incorrect',
    )

