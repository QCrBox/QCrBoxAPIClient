*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client for data files endpoints

# Resources -- implemented in Robot
Resource            resources/keywords.resource
Library             OperatingSystem
Library             libraries/endpoints/data_files.py
Library             libraries/endpoints/datasets.py

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes


*** Variables ***
${REGISTRY_ADDRESS}     %{QCRBOX_BIND_ADDRESS=127.0.0.1}
${REGISTRY_PORT}        %{QCRBOX_REGISTRY_PORT=11000}
${API_BASE_URL}         http://${REGISTRY_ADDRESS}:${REGISTRY_PORT}
${API_CLIENT}           ${EMPTY}
${TEST_FILE_PATH}       test_data/api_client_test_cif.cif
${TEST_FILE_NAME}       api_client_test_cif.cif
${TEST_DATASET_ID}      ${EMPTY}
${TEST_DATA_FILE_ID}    ${EMPTY}


*** Test Cases ***
Check create_data_file uploads a file
    ${body}=    Construct Create Data File Body    ${TEST_FILE_PATH}
    ${response}=    Create Data File    ${API_CLIENT}    ${body}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    data_files
    ${data_files}=    Set Variable    ${response.payload.data_files}
    Length Should Be
    ...    ${data_files}
    ...    1
    ...    "create_data_file API call return an incorrect number of data files when it should return only the created data file"
    ${test_data_file_id}=    Set Variable    ${response.payload.data_files[0].qcrbox_file_id}
    Set Suite Variable    ${TEST_DATA_FILE_ID}    ${test_data_file_id}

Check list_data_files returns list of data_files
    ${response}=    List Data Files    ${API_CLIENT}
    Check For Error Response    ${response}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    data_files
    ${data_files}=    Set Variable    ${response.payload.data_files}
    ${n_data_files}=    Get Length    ${data_files}
    Should Be True    ${n_data_files} > 0    "No data files were retrieved, when there should be at least 1"

    Check Data Files Structure    @{response.payload.data_files}

Check get_data_file_by_id returns a data file
    ${response}=    Get Data File By Id    ${API_CLIENT}    ${TEST_DATA_FILE_ID}
    Check For Error Response    ${response}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    data_files
    ${data_files}=    Set Variable    ${response.payload.data_files}
    Length Should Be    ${data_files}    1    "Requested 1 data file, but multiple (or none) were returned"

    Check Data Files Structure    @{data_files}
    ${data_file}=    Set Variable    ${data_files[0]}
    Should Be Equal    ${data_file.qcrbox_file_id}    ${TEST_DATA_FILE_ID}

Check that download_data_file_by_id downloads a file
    ${response}=    Download Data File By Id    ${API_CLIENT}    ${TEST_DATA_FILE_ID}
    Should Not Be None    ${response}

    ${file_contents}=    Get File    ${TEST_FILE__PATH}
    Should Be Equal As Strings    ${file_contents}    ${response}

Check get_file_by_id returns 404 for incorrect id
    ${response}=    Get Data File By Id    ${API_CLIENT}    trousers
    Check Response Has Attributes    ${response}    status    error

    ${error_payload}=    Set Variable    ${response.error}
    Check Response Has Attributes    ${error_payload}    code    message    details
    Should Be Equal    ${{int(404)}}    ${error_payload.code}

Check that delete_data_file_by_id deletes a data file
    ${response}=    Delete Data File By Id    ${API_CLIENT}    ${TEST_DATA_FILE_ID}
    Check For Error Response    ${response}

Check download_data_file_by_id returns 404 for deleted dataset
    ${response}=    Download Data File By Id    ${API_CLIENT}    ${TEST_DATA_FILE_ID}
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

Check Data Files Structure
    [Arguments]    @{data_files}

    FOR    ${data_file}    IN    @{data_files}
        Check Response Has Attributes    ${data_file}    qcrbox_file_id    filename    filetype
    END
