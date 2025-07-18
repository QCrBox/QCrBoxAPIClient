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
${REGISTRY_ADDRESS}     %{QCRBOX_BIND_ADDRESS=127.0.0.1}
${REGISTRY_PORT}        %{QCRBOX_REGISTRY_PORT=11000}
${API_BASE_URL}         http://${REGISTRY_ADDRESS}:${REGISTRY_PORT}
${API_CLIENT}               ${EMPTY}
${TEST_CALCULATION_ID}      ${EMPTY}


*** Test Cases ***
Check list_calculations returns a list of calculations
    ${response}=    List Calculations    ${API_CLIENT}
    Check For Error Response    ${response}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    calculations
    ${calculations}=    Set Variable    ${response.payload.calculations}
    ${n_calculations}=    Get Length    ${calculations}
    Should Be True    ${n_calculations} > 0    "No calculations retrieved, when we are expecting at least 1"
    Check Calculations Structure    ${calculations}

    Set Suite Variable    ${TEST_CALCULATION_ID}    ${calculations[0].calculation_id}

Check get_calculation_by_id returns a calculation
    ${response}=    Get Calculation By Id    ${API_CLIENT}    ${TEST_CALCULATION_ID}
    Check For Error Response    ${response}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    calculations
    ${calculations}=    Set Variable    ${response.payload.calculations}
    ${n_calculations}=    Get Length    ${calculations}
    Should Be True    ${n_calculations} == 1    "Multiple calculations retrieved, when only one requested"

    Check Calculations Structure    ${calculations}

Check get_calculation_by_id returns 404 for incorrect id
    ${response}=    Get Calculation By Id    ${API_CLIENT}    -1
    Check Response Has Attributes    ${response}    status    error

    ${error_payload}=    Set Variable    ${response.error}
    Check Response Has Attributes    ${error_payload}    code    message    details
    Should Be Equal    ${{int(404)}}    ${error_payload.code}


*** Keywords ***
Setup suite
    Log datetime information
    Log    Starting test suite
    ${client}=    Create API Client    ${API_BASE_URL}
    Set Suite Variable    ${API_CLIENT}    ${client}

Teardown suite
    Log datetime information
    Log    Test suite completed

Check Calculations Structure
    [Arguments]    ${calculations}

    FOR    ${calculation}    IN    @{calculations}
        Check Response Has Attributes
        ...    ${calculation}
        ...    calculation_id
        ...    application_slug
        ...    application_version
        ...    command_name
        ...    status
        ...    arguments
    END
