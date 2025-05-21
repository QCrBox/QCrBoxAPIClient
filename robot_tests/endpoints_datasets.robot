*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client datasets endpoints

# Resources -- implemented in Robot
Resource            resources/keywords.resource
# Standard libraries
Library    Collections
# API glue code -- implemented in Python
Library             libraries/endpoints/datasets.py

Suite Setup    Setup Suite
Suite Teardown    Teardown Suite
Test Timeout        2 minutes

*** Variables ***
${API_BASE_URL}                 http://127.0.0.1:11000/
${API_CLIENT}                   ${EMPTY}
${TEST_FILE_PATH}               test_data/api_client_test_cif.cif
${TEST_FILE_NAME}               api_client_test_cif.cif
${TEST_FILE_CONTENT_TYPE}       text/cif
${TEST_DATASET_ID}              ${EMPTY}


*** Test Cases ***
Check create_datasets can upload a data file
    ${body}=    Create File Upload Body    ${TEST_FILE_PATH}
    ${response}=    Create Dataset    ${API_CLIENT}    ${body}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    datasets
    ${datasets}=    Set Variable    ${response.payload.datasets}
    Length Should Be
    ...    ${datasets}
    ...    1
    ...    "create_datasets API call return an incorrect number of datasets when it should return only the created dataset"
    ${test_dataset_id}=    Set Variable    ${response.payload.datasets[0].qcrbox_dataset_id}
    Set Suite Variable    ${TEST_DATASET_ID}    ${test_dataset_id}

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

    Check Response Has Attributes    ${response.payload}    datasets
    ${datasets}=    Set Variable    ${response.payload.datasets}
    Length Should Be
    ...    ${datasets}
    ...    1
    ...    "get_datasets_by_id API call return an incorrect number of datasets when it should return only the created dataset"
    ${dataset_id}=    Set Variable    ${response.payload.datasets[0].qcrbox_dataset_id}
    Should Be Equal    ${TEST_DATASET_ID}    ${dataset_id}    "get_datasets_by_id returned the wrong dataset"

Check delete_dataset can delete a dataset
   Delete Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}

Check get_dataset_by_id returns 404 for deleted dataset
    ${response}=    Get Dataset By Id    ${API_CLIENT}    ${TEST_DATASET_ID}
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
