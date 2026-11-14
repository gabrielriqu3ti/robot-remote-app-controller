*** Settings ***
Documentation  Resource to communicate to remote controlled app.
Library        libraries/RemoteAppGrpcClient.py

*** Keywords ***
Connect to App
    Connect    localhost    50051

Disconnect from App
    Disconnect

