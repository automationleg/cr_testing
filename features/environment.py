import logging
import os

# absolute path to this directory containing environment file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ALLURE_RESULTS_DIR = os.path.join(ROOT_DIR, 'test_reports')


def generate_allure_properties(**env_kwargs):
    """
    Create environment.properties file with provided key:value pairs to be displayed in the allure report
    :param env_kwargs: keyword arguments to include ie: 'ENVIRONMENT':'DEV'
    :return: None
    """
    file_path = os.path.join(ALLURE_RESULTS_DIR, 'environment.properties')
    with open(file_path, 'a') as properties_file:
        for key, value in env_kwargs.items():
            properties_file.write(f'{key}:{value}\n')


def before_all(context):
    context.config.setup_logging()

    env_urls = {
        'DEV': os.environ.get("SITE_URL_DEV"),
    }

    # set environment to DEV by default in case no environment variable set
    environment = os.environ.get("ENVIRONMENT", "DEV")
    context.site_base_url = env_urls[environment]

    # authentication
    context.api_key = os.environ.get("API_KEY")
    context.api_sec = os.environ.get("API_SEC")
    context.api_otp = os.environ.get("API_OTP")

    # set allure properties file
    environment_properties = {
        'environment': environment,
        'API URL': context.site_base_url,
    }
    # generate_allure_properties(**environment_properties)


def before_scenario(context, scenario):
    logging.info(f'Running scenario: <{scenario.name}>')


def after_scenario(context, scenario):
    if context.failed:
        logging.info(f'Scenario {context.scenario} - FAILED')
    else:
        logging.info(f'Scenario {context.scenario} - PASSED')
