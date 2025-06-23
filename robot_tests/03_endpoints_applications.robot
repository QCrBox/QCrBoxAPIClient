*** Settings ***
Documentation
...                 Test suite for QCrBox Python API Client applications endpoints

# Resources -- implemented in Robot
Resource            resources/keywords.resource
# API glue code -- implemented in Python
Library             libraries/endpoints/applications.py

Suite Setup         Setup suite
Suite Teardown      Teardown suite
Test Timeout        2 minutes


*** Variables ***
${API_BASE_URL}     http://127.0.0.1:11000/
${API_CLIENT}       ${EMPTY}


*** Test Cases ***
Check list_applications returns applications
    ${response}=    List Applications    ${API_CLIENT}
    Check Response Structure    ${response}

    Check Response Has Attributes    ${response.payload}    applications
    ${applications}=    Set Variable    ${response.payload.applications}
    ${n_applications}=    Get Length    ${applications}
    Should Be True    ${n_applications} > 0    "No registered applications, which is unexpected"
    Check Applications Structure    @{applications}


*** Keywords ***
Setup suite
    Log datetime information
    Log    Starting test suite
    ${client}=    Create API Client    ${API_BASE_URL}
    Set Suite Variable    ${API_CLIENT}    ${client}

Teardown suite
    Log datetime information
    Log    Test suite completed

Check Applications Structure
    [Arguments]    @{applications}
    FOR    ${application}    IN    @{applications}
        Check Response Has Attributes
        ...    ${application}
        ...    name
        ...    slug
        ...    version
        ...    description
        ...    url
        ...    registered_at
        ...    commands
        ...    gui_port
        FOR    ${command}    IN    @{application.commands}
            Check Response Has Attributes    ${command}    name    description    implemented_as    parameters
        END
    END
