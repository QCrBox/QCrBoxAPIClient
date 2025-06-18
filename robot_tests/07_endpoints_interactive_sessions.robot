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
${API_BASE_URL}                     http://127.0.0.1:11000/
${API_CLIENT}                       ${EMPTY}
${TEST_FILE_PATH}                   test_data/api_client_test_cif.cif
${TEST_FILE_NAME}                   api_client_test_cif.cif
${TEST_FILE_CONTENT_TYPE}           text/cif
${TEST_DATASET_ID}                  ${EMPTY}
${TEST_DATA_FILE_ID}                ${EMPTY}
${TEST_INTERACTIVE_SESSION_ID}      ${EMPTY}


*** Test Cases ***
Check list_interactive_sessions returns a list of sessions
    ${response}=    List Interactive Sessions    ${API_CLIENT}
    Check For Error Response    ${response}

    Check Response Structure    ${response}
    Check Response Has Attributes    ${response.payload}    interactive_sessions
    ${interactive_sessions}=    Set Variable    ${response.payload.interactive_sessions}
    Check Interactive Sessions Structure    @{interactive_sessions}

Check create_interactive_session_with_arguments can create an interactive session
    ${input_file}=    Create Dictionary    data_file_id=${TEST_DATA_FILE_ID}
    ${arguments}=    Create Dictionary    input_file=${input_file}
    ${create_body}=    Create Interactive Session Create Body    olex2    1.5-alpha    ${arguments}

    ${response}=    Create Interactive Session With Arguments    ${API_CLIENT}    ${create_body}
    Check For Error Response    ${response}

    Sleep    3s    "Waiting for interactive session to be registered"

    Check Response Structure    ${response}
    Check Response Has Attributes    ${response.payload}    interactive_session_id
    Set Suite Variable    ${TEST_INTERACTIVE_SESSION_ID}    ${response.payload.interactive_session_id}

Check create_interactive_session_with_arguments fails for incorrect request
    ${input_file}=    Create Dictionary    data_file_id=${TEST_DATA_FILE_ID}
    ${arguments}=    Create Dictionary    input_file=${input_file}
    ${create_body}=    Create Interactive Session Create Body    olex-999    1.5-alpha    ${arguments}

    ${response}=    Create Interactive Session With Arguments    ${API_CLIENT}    ${create_body}
    Check Response Has Attributes    ${response}    status
    Should Be Equal    ${response.status}    error

Check that get_interactive_session_by_id returns interactive session
    ${response}=    Get Interactive Session By Id    ${API_CLIENT}    ${TEST_INTERACTIVE_SESSION_ID}
    Check For Error Response    ${response}

    Check Response Structure    ${response}
    Check Response Has Attributes    ${response.payload}    interactive_sessions

    ${interactive_session}=    Set Variable    ${response.payload.interactive_sessions}
    Check Interactive Sessions Structure    @{interactive_session}

Check that get_interactive_session_by_id returns 404 for incorrect id
    ${response}=    Get Interactive Session By Id    ${API_CLIENT}    1

    Check Response Has Attributes    ${response}    status    error
    Check Response Has Attributes    ${response.error}    code    message    details
    Should Be Equal    ${response.error.code}    ${{int(404)}}

Check that an interactive session can be closed
    ${response}=    Close Interactive Session    ${API_CLIENT}    ${TEST_INTERACTIVE_SESSION_ID}
    Check For Error Response    ${response}

    Check Response Structure    ${response}
    Check Response Has Attributes    ${response.payload}    interactive_sessions

    ${interactive_sessions}=    Set Variable    ${response.payload.interactive_sessions[0]}
    Check Response Has Attributes    ${interactive_sessions}    session_id    status    output_dataset_id


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

Check Interactive Sessions Structure
    [Arguments]    @{interactive_sessions}

    FOR    ${interactive_session}    IN    @{interactive_sessions}
        Check Response Has Attributes
        ...    ${interactive_session}
        ...    session_id
        ...    client_private_inbox
        ...    application_slug
        ...    application_version
        ...    command_name
        ...    arguments
    END
