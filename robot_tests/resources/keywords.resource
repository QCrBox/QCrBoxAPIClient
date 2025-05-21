*** Settings ***
Library    DateTime
Library     ../libraries/my_keywords.py
Library    ../libraries/client.py

*** Keywords ***
Create API Client
    [Arguments]    ${base_url}
    ${client}=    Get Sync Client    ${base_url}
    RETURN    ${client}

Log datetime information
    ${date}=    Get Current Date
    Log    ${date}

Check Response Structure
    [Arguments]    ${response}
    Check Object Has Attributes    ${response}    status    message    timestamp    payload

Check Response Has Attributes
    [Arguments]    ${payload}    @{attribute}
    Check Object Has Attributes    ${payload}    @{attribute}
