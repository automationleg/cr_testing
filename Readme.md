# Welcome to Testing API Project

## Test Project Structure
```
\features
    ├── api_objects
    ├── json_schemas
    ├── steps
    └── test_scenarios
```

api_objects     - api objects and helper functions
json_schemas    - files with json schemas used to validate api responses
steps           - behave test steps
test_scenarios  - behave feature files with test scenarios

## Environment setup
Execution of tests that utilize public endpoint doesn't require authentication

The following environment variables are required to execute tests inside docker container against private endpoints  

API_KEY  - authentication key  
API_SEC  - secure private key  
API_OTP  - secure password for 2FA auth  
SITE_URL - main api url 

Install Allure reports - follow steps in [Reporting](##reporting) section

## Test Execution with Docker
local docker engine or docker desktop app is required to run the following commands
1. Build an image
```shell
docker build -t cr_testing .
```
2. Execute tests
```shell
docker run --rm -e SITE_URL=<YOUR_SITE_URL>
    -e API_KEY=<YOUR_API_KEY> \
    -e API_SEC=<YOUR_API_SEC> \
    -e API_OTP=<YOUR_API_OTP> \
    -v $(pwd)/test_reports:/test_reports cr_testing
```
Allure reports are being generated into `test_reports` directory after tests run completes

3. Display generated Allure test report
```shell
allure serve test_reports
```

## Reporting

Behave has ability to create xml reports for each ran Scenario and junit reports for Jenkins or other CI integration. Local execution reporting is based on Allure solution.
In order to run test with Allure reports follow the steps:

1. (Windows only) Install Scoop
`iex (new-object net.webclient).downloadstring("'https://get.scoop.sh")`

if permissions error occures, execute following command and repeat the step
`Set-ExecutionPolicy RemoteSigned -scope CurrentUser`

2. Install allure 

Windows: `scoop install allure`
MacOS:	 `brew install allure`	

3. Install Java (for spinning web service)

4. Run tests locally with allure reporting
`behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features`

5. Based on reports, spin up allure portal

`allure serve %allure_result_folder%`

## Credits
To all folks who will spent time reviewing it