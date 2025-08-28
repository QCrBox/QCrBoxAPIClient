*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client datasets endpoints

Library             Collections
Library             OperatingSystem
Library             libraries/endpoints/datasets.py
Library             libraries/endpoints/data_files.py
Resource            resources/keywords.resource

Suite Setup         Setup Suite
Suite Teardown      Teardown Suite
Test Timeout        2 minutes


*** Variables ***
${REGISTRY_ADDRESS}         %{QCRBOX_BIND_ADDRESS=127.0.0.1}
${REGISTRY_PORT}            %{QCRBOX_REGISTRY_PORT=11000}
${API_BASE_URL}             http://${REGISTRY_ADDRESS}:${REGISTRY_PORT}
${API_CLIENT}               ${EMPTY}
${TEST_CIF_FILE_PATH}       test_data/api_client_test_cif.cif
${TEST_CIF_FILE_NAME}       api_client_test_cif.cif
${TEST_JSON_FILE_PATH}      test_data/api_client_test_json.json
${TEST_JSON_FILE_NAME}      api_client_test_json.json
${TEST_DATASET_ID}          ${EMPTY}
${TEST_JSON_FILE_ID}        ${EMPTY}


*** Test Cases ***
Check create_datasets can upload a data file
    ${body}=    Construct Create Dataset Body    ${TEST_CIF_FILE_PATH}
    ${response}=    Create Dataset    ${API_CLIENT}    ${body}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    datasets    data_files
    ${datasets}=    Set Variable    ${response.payload.datasets}
    Length Should Be
    ...    ${datasets}
    ...    1
    ...    "create_datasets API call return an incorrect number of datasets when it should return only the created dataset"
    ${test_dataset_id}=    Set Variable    ${response.payload.datasets[0].qcrbox_dataset_id}
    Set Suite Variable    ${TEST_DATASET_ID}    ${test_dataset_id}

Check append_to_dataset can add a file to a dataset
    ${body}=    Construct Append To Dataset Body    ${TEST_JSON_FILE_PATH}
    ${response}=    Append To Dataset    ${API_CLIENT}    ${TEST_DATASET_ID}    ${BODY}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    datasets    data_files    appended_file
    Length Should Be
    ...    ${response.payload.datasets}
    ...    1
    ...    "append_to_dataset returned an incorrect number of datasets when it should only return the updated dataset"

    ${dataset}=    Set Variable    ${response.payload.datasets[0]}
    ${data_files}=    Set Variable    ${dataset.data_files.to_dict()}
    Length Should Be
    ...    ${data_files}
    ...    2
    ...    "Should be 2 data files in the test dataset (the CIF and the JSON file)"
    Set Suite Variable    ${TEST_JSON_FILE_ID}    ${data_files["${TEST_JSON_FILE_NAME}"]['qcrbox_file_id']}

Check list_datasets returns datasets
    ${response}=    List Datasets    ${API_CLIENT}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    datasets
    ${n_datasets}=    Get Length    ${response.payload.datasets}
    Should Be True    ${n_datasets} > 0    "No datasets retrieved, even though at least one has been uploaded"
    ${datasets}=    Set Variable    ${response.payload.datasets}
    Check Datasets Structure    @{datasets}

Check get_dataset_by_id returns the correct dataset
    ${response}=    Get Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    datasets    data_files
    ${datasets}=    Set Variable    ${response.payload.datasets}
    Length Should Be
    ...    ${datasets}
    ...    1
    ...    "get_datasets_by_id API call return an incorrect number of datasets when it should return only the created dataset"
    ${dataset_id}=    Set Variable    ${response.payload.datasets[0].qcrbox_dataset_id}
    Should Be Equal    ${TEST_DATASET_ID}    ${dataset_id}    "get_datasets_by_id returned the wrong dataset"

Check that download_dataset_by_id downloads a zip file for datasets with multiple files
    ${response}=    Download Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}
    Should Not Be None    ${response}

    Create Binary File    /tmp/robot.zip    ${response}
    Validate Is Zip    /tmp/robot.zip
    Remove File    /tmp/robot.zip

Check that deleting a data file removes it from the dataset
    ${response}=    Delete Data File By Id    ${API_CLIENT}    ${TEST_JSON_FILE_ID}
    ${response}=    Get Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}

    ${dataset}=    Set Variable    ${response.payload.datasets[0]}
    ${data_files}=    Set Variable    ${dataset.data_files.to_dict()}
    Length Should Be    ${data_files}    1    "JSON file was not deleted from dataset"

Check that download_dataset_by_id downloads a file for datasets with a single file
    ${response}=    Download Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}
    Should Not Be None    ${response}

    ${file_contents}=    Get File    ${TEST_CIF_FILE_PATH}
    Should Be Equal As Strings    ${file_contents}    ${response}

Check delete_dataset can delete a dataset
    ${response}=    Delete Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}
    IF    ${response}    Check For Error Response    ${response}

Check get_dataset_by_id returns 404 for deleted dataset
    ${response}=    Get Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}
    Check Response Has Attributes    ${response}    status    error

    ${error_payload}=    Set Variable    ${response.error}
    Check Response Has Attributes    ${error_payload}    code    message    details
    Should Be Equal    ${{int(404)}}    ${error_payload.code}

Check download_dataset_by_id returns 404 for deleted dataset
    ${response}=    Download Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}
    Check Response Has Attributes    ${response}    status    error

    ${error_payload}=    Set Variable    ${response.error}
    Check Response Has Attributes    ${error_payload}    code    message    details
    Should Be Equal    ${{int(404)}}    ${error_payload.code}


*** Keywords ***
Setup Suite
    Log datetime information
    Log    Starting test suite
    ${client}=    Create API Client    ${API_BASE_URL}
    Set Suite Variable    ${API_CLIENT}    ${client}

Teardown Suite
    Log datetime information
    Log    Test suite completed

Check Datasets Structure
    [Arguments]    @{datasets}

    FOR    ${dataset}    IN    @{datasets}
        Check Response Has Attributes    ${dataset}    qcrbox_dataset_id    data_files
    END
