import logging
import os

# absolute path to this directory containing environment file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ALLURE_RESULTS_DIR = os.path.join(ROOT_DIR, 'test_reports')


def before_all(context):
    context.config.setup_logging()

    # In general this would normally be defined as constant url per environment instead of env variable
    context.site_base_url = os.environ.get("SITE_URL")

    # authentication
    context.api_key = os.environ.get("API_KEY")
    context.api_sec = os.environ.get("API_SEC")
    context.api_otp = os.environ.get("API_OTP")


def before_scenario(context, scenario):
    logging.info(f'Running scenario: <{scenario.name}>')


def after_scenario(context, scenario):
    if context.failed:
        logging.info(f'Scenario {context.scenario} - FAILED')
    else:
        logging.info(f'Scenario {context.scenario} - PASSED')
