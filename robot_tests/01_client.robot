*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client

# Resources -- implemented in Robot
Resource    resources/keywords.resource

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes

*** Variables ***
${REGISTRY_ADDRESS}     %{QCRBOX_BIND_ADDRESS=127.0.0.1}
${REGISTRY_PORT}        %{QCRBOX_REGISTRY_PORT=11000}
${BASE_URL}             http://${REGISTRY_ADDRESS}:${REGISTRY_PORT}


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
