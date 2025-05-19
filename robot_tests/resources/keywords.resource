*** Settings ***
Library     ../libraries/my_keywords.py


*** Keywords ***
Check Response Structure
    [Arguments]    ${response}
    Check Object Has Attributes    ${response}    status    message    timestamp    payload

Check Response Has Attributes
    [Arguments]    ${payload}    @{attribute}
    Check Object Has Attributes    ${payload}    @{attribute}

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
        FOR    ${command}    IN    @{application.commands}
            Check Response Has Attributes    ${command}    name    description    implemented_as    parameters
        END
    END
