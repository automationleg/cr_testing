import time

from behave import step

from features.api_objects.private import UserData, Auth


@step('Request is sent to get "{endpoint_uri}" User Data')
def step_impl(context, endpoint_uri):
    payload_data = {
        "nonce": str(int(1000*time.time())),
        "otp": context.api_otp,
        "trades": True,
    }

    auth = Auth(uri=endpoint_uri,
                api_key=context.api_key,
                api_secret=context.api_sec,
                payload_data=payload_data,
                )
    user_data = UserData(f"{context.site_base_url}", auth=auth)

    context.response = user_data.get_data(endpoint_uri, payload_data)
