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
${COMMAND_ID}       ${EMPTY}


*** Test Cases ***
Check list_commands returns list of commands
    ${response}=    List Commands    ${API_CLIENT}
    Check For Error Response    ${response}
    Check Response Structure    ${response}

    Check Object Has Attributes    ${response.payload}    commands
    ${commands}=    Set Variable    ${response.payload.commands}
    Check Commands Structure    @{commands}

Check get_command_by_id returns a command
    ${response}=    Get Command By Id    ${API_CLIENT}    ${COMMAND_ID}
    Check For Error Response    ${response}
    Check Response Structure    ${response}

    Check Object Has Attributes    ${response.payload}    commands
    ${commands}=    Set Variable    ${response.payload.commands}
    Check Commands Structure    @{commands}

Check get_command_by_id returns 404 for incorrect id
    ${response}=    Get Command By Id    ${API_CLIENT}    -1
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

Check Commands Structure
    [Arguments]    @{commands}

    FOR    ${command}    IN    @{commands}
        Log    ${command}
        Check Response Has Attributes
        ...    ${command}
        ...    name
        ...    implemented_as
        ...    parameters
        ...    id
        ...    application_id
        ...    application
        ...    version
        ...    cmd_name
        ...    description
        ...    merge_cif_su
        ...    doi
        ${parameters}=    Get Command Parameter Names    ${command.parameters}
        ${n_parameters}=    Get Length    ${parameters}
        Should Be True    ${n_parameters} > 0    "Command with no parameters is invalid"
        Set Suite Variable    ${COMMAND_ID}    ${command.id}
    END
