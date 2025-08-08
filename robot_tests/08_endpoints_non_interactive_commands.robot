*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client for interactive sessions endpoints

# Resources -- implemented in Robot
Resource            resources/keywords.resource
# Libraries
Library             libraries/endpoints/calculations.py
Library             libraries/endpoints/commands.py
Library             libraries/endpoints/datasets.py

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes


*** Variables ***
${REGISTRY_ADDRESS}         %{QCRBOX_BIND_ADDRESS=127.0.0.1}
${REGISTRY_PORT}            %{QCRBOX_REGISTRY_PORT=11000}
${API_BASE_URL}             http://${REGISTRY_ADDRESS}:${REGISTRY_PORT}
${API_CLIENT}               ${EMPTY}
${TEST_CALCULATION_ID}      ${EMPTY}


*** Test Cases ***
Check invoke_command can invoke a non-interactive command
    ${arguments}=    Create Dictionary    dummy="hello"
    ${create_body}=    Create Invoke Command Body    dummy_cli    0.1.0    infinite_loop    ${arguments}

    ${response}=    Invoke Command    ${API_CLIENT}    ${create_body}
    Check For Error Response    ${response}
    Check Response Structure    ${response}
    Check Response Has Attributes    ${response.payload}    calculation_id

    Set Suite Variable    ${TEST_CALCULATION_ID}    ${response.payload.calculation_id}

Check that a running calculation can be stopped
    ${response}=    Stop Running Calculation    ${API_CLIENT}    ${TEST_CALCULATION_ID}
    ${response}=    Get Calculation By Id    ${API_CLIENT}    ${TEST_CALCULATION_ID}
    Should Be Equal    ${response.payload.calculations[0].status}    successful


*** Keywords ***
Setup suite
    Log datetime information
    Log    Starting test suite
    ${client}=    Create API Client    ${API_BASE_URL}
    Set Suite Variable    ${API_CLIENT}    ${client}

Teardown suite
    Log datetime information
    Log    Test suite completed
