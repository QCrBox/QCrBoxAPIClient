*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client for calculations endpoints

# Resources -- implemented in Robot
Resource            resources/keywords.resource
# Libraries -- endpoints wrappers
Library    libraries/endpoints/calculations.py

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes

*** Variables ***
${API_BASE_URL}     http://127.0.0.1:11000/
${API_CLIENT}       ${EMPTY}


*** Test Cases ***
Check list_calculations returns a list of calculations
    ${response}=    List Calculations    ${API_CLIENT}
    Check For Error Response    ${response}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    calculations
    ${calculations}=    Set Variable    ${response.payload.calculations}
    ${n_calculations}=    Get Length    ${calculations}
    Should Be True    ${n_calculations} > 0    "No calculations retrieved, when we are expecting at least 1"


*** Keywords ***
Setup suite
    Log datetime information
    Log    Starting test suite
    ${client}=    Create API Client    ${API_BASE_URL}
    Set Suite Variable    ${API_CLIENT}    ${client}

Teardown suite
    Log datetime information
    Log    Test suite completed
