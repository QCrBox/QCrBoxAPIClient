*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client for interactive sessions endpoints

# Resources -- implemented in Robot
Resource            resources/keywords.resource
# Libraries
Library    libraries/endpoints/interactive_sessions.py
Library    libraries/endpoints/datasets.py

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes

*** Variables ***
${API_BASE_URL}                 http://127.0.0.1:11000/
${API_CLIENT}                   ${EMPTY}
${TEST_FILE_PATH}               test_data/api_client_test_cif.cif
${TEST_FILE_NAME}               api_client_test_cif.cif
${TEST_FILE_CONTENT_TYPE}       text/cif
${TEST_DATASET_ID}              ${EMPTY}
${TEST_DATA_FILE_ID}            ${EMPTY}


*** Test Cases ***
Check that an interactive session can be created
    ${input_file}=    Create Dictionary    data_file_id=${TEST_DATA_FILE_ID}
    ${arguments}=    Create Dictionary    input_file=${input_file}
    ${create_body}=    Create Interactive Session Create Body    olex2    1.5-alpha    ${arguments}

    ${response}=    Create Interactive Session With Arguments    ${API_CLIENT}    ${create_body}

    Log    ${response}


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
