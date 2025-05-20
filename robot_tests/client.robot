*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client

# Resources -- implemented in Robot
Resource    resources/keywords.resource

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes

*** Variables ***
${BASE_URL}     http://127.0.0.1:11000/


*** Test Cases ***
Check that a client can be created
    ${client}=    Create API Client    ${BASE_URL}
    Should Not Be None    ${client}    Client


*** Keywords ***
Setup suite
    Log datetime information
    Log    Starting test suite

Teardown suite
    Log datetime information
    Log    Test suite completed
