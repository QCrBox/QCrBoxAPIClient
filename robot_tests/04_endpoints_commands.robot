*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client for commands endpoints

# Resources -- implemented in Robot
Resource            resources/keywords.resource
Library    libraries/endpoints/commands.py

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes

*** Variables ***
${API_BASE_URL}     http://127.0.0.1:11000/
${API_CLIENT}       ${EMPTY}


*** Test Cases ***
Check list_commands returns list of commands
    ${response}=    List Commands    ${API_CLIENT}



*** Keywords ***
Setup suite
    Log datetime information
    Log    Starting test suite
    ${client}=    Create API Client    ${API_BASE_URL}
    Set Suite Variable    ${API_CLIENT}    ${client}

Teardown suite
    Log datetime information
    Log    Test suite completed
