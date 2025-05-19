*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client

# From standard library
Library             DateTime
# Resources -- implemented in Robot
Resource            resources/keywords.resource
# API glue code -- implemented in Python
Library             libraries/client.py
Library             libraries/endpoints/applications.py

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes


*** Variables ***
${BASE_URL}     http://127.0.0.1:11000/


*** Test Cases ***
Check that a client can be created
    ${client}=    Create API Client
    Should Not Be None    ${client}    Client

Check list_applications returns applications
    ${client}=    Create API Client
    ${response}=    List Applications    ${client}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    applications
    ${applications}=    Set Variable    ${response.payload.applications}
    ${n_applications}=    Get Length    ${applications}
    Should Be True    ${n_applications} > 0    "No registered applications, which is unexpected"
    Check Applications Structure    @{applications}


*** Keywords ***
Create API Client
    ${client}=    Get Sync Client    ${BASE_URL}
    RETURN    ${client}

Log datetime information
    ${date}=    Get Current Date
    Log    ${date}

Setup suite
    Log datetime information
    Log    Starting test suite

Teardown suite
    Log datetime information
    Log    Test suite completed
