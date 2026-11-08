*** Settings ***
Documentation  This is a resource file, that can contain variables and keywords.
...            Keywords defined here can be used where this keywords.resource is loaded.
Library        libraries/CustomLibrary.py

*** Keywords ***
Connect to Server
    Connect  127.0.0.1

Close Server Connection
    Disconnect

Login User
    [Arguments]     ${name}  ${password}
    Set Login Name  ${name}
    Set Password    ${password}
    Execute Login

Verify Valid Login
    [Arguments]    ${expected_username}
    ${version}=  Get Server Version
    Should Not Be Empty  ${version}
    ${username}=  Get User Name
    Should Be Equal  ${username}  ${expected_username}

Verify Unauthorized Access
    Run Keyword And Expect Error  PermissionError*  Get Server Version

    