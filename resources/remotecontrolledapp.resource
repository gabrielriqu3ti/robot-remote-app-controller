*** Settings ***
Documentation  Resource to communicate to remote controlled app.
Library        libraries/RemoteAppGrpcClient.py

*** Keywords ***
Connect to App
    Connect    localhost    50051

Disconnect from App
    Disconnect

Take Screenshot
    [Arguments]        ${filename}
    Save Screenshot    ${filename}
    Log                <img src=${filename} width="900px">    html=True

Manual Action
    [Arguments]       @{args}
    Log to Console    @{args}