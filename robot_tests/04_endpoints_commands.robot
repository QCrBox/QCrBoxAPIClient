*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client for commands endpoints

# Resources -- implemented in Robot
Resource            resources/keywords.resource
Library    libraries/endpoints/commands.py
Library    libraries/endpoints/datasets.py

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes

*** Variables ***
${REGISTRY_ADDRESS}     %{QCRBOX_BIND_ADDRESS=127.0.0.1}
${REGISTRY_PORT}        %{QCRBOX_REGISTRY_PORT=11000}
${API_BASE_URL}         http://${REGISTRY_ADDRESS}:${REGISTRY_PORT}
${API_CLIENT}           ${EMPTY}
${COMMAND_ID}           ${EMPTY}
${TEST_FILE_PATH}       test_data/api_client_test_cif.cif
${TEST_FILE_NAME}       api_client_test_cif.cif
${TEST_DATASET_ID}      ${EMPTY}
${TEST_DATA_FILE_ID}    ${EMPTY}


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

Check invoke_command can invoke a non-interactive command
    ${input_file}=    Create Dictionary    data_file_id=${TEST_DATA_FILE_ID}
    ${arguments}=    Create Dictionary    input_cif=${input_file}    output_cif_path=/opt/qcrbox/test_unified_cif.cif
    ${create_body}=    Create Invoke Command Body    qcrboxtools    0.0.5    to_unified_cif    ${arguments}

    ${response}=    Invoke Command    ${API_CLIENT}    ${create_body}
    Check For Error Response    ${response}

    Sleep    1s    "Waiting for non-interactive command to start and be registered"

    Check Response Structure    ${response}
    Check Response Has Attributes    ${response.payload}    calculation_id


*** Keywords ***
Setup suite
    Log datetime information
    Log    Starting test suite
    ${client}=    Create API Client    ${API_BASE_URL}
    Set Suite Variable    ${API_CLIENT}    ${client}

    ${file_upload}=    Upload Test Dataset
    Set Suite Variable    ${TEST_DATASET_ID}    ${file_upload[0]}
    Set Suite Variable    ${TEST_DATA_FILE_ID}    ${file_upload[1]}

Teardown suite
    Delete Test Dataset
    Log datetime information
    Log    Test suite completed

Upload Test Dataset
    ${body}=    Create File Upload Body    ${TEST_FILE_PATH}
    ${response}=    Create Dataset    ${API_CLIENT}    ${body}
    ${dataset}=    Set Variable    ${response.payload.datasets[0]}
    ${data_file}=    Set Variable    ${dataset.data_files['${TEST_FILE_NAME}']}
    RETURN    ${dataset.qcrbox_dataset_id}    ${data_file.qcrbox_file_id}

Delete Test Dataset
    Delete Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}

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
