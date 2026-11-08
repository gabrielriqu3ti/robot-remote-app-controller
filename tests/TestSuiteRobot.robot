*** Settings ***
Documentation  A test suite for valid login.
...
...            Keys are imported from the resource file.
Resource       resources/keywords.resource
Default Tags   positive


*** Test Cases ***
Login User With Password
    Connect to Server
    Login User            ironman  1234567890
    Verify Valid Login    Tony Stark
    [Teardown]  Close Server Connection


Deny Login With Wrong Password
    [Tags]  negative
    Connect to Server
    Run Keyword And Expect Error  *Invalid Password  Login User  ironman  123
    Verify Unauthorized Access 
    [Teardown]  Close Server Connection
