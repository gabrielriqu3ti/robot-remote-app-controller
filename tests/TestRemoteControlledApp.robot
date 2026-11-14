*** Settings ***
Documentation    A test suite to test a remote controlled app.
Resource         resources/remotecontrolledapp.resource
Test Setup       Connect to App
Test Teardown    Disconnect from App
Test Tags        positive


*** Test Cases ***
Test Text Field Can Be Written
    [Tags]             requirement 1
    ${text}=           Type Text    App.JTextField.inputText    Text typed into Text Field.
    Should Be Equal    ${text}    Text typed into Text Field.

Test Button Can Be Clicked
    [Tags]             requirement 2
    Click              App.JButton.copyText

Test Button Copies Text Written at Text Field to Label
    [Tags]             requirement 3
    Type Text          App.JTextField.inputText    Text to be copied.
    Click              App.JButton.copyText
    ${text}=           Get Text    App.JLabel.copiedText
    Should Be Equal    ${text}    Text to be copied.

Failed Test Button Copies Text Written at Text Field to Label
    [Documentation]    This test is meant to fail to show how the robot works.
    [Tags]             requirement 3    -positive    negative
    Type Text          App.JTextField.inputText    Text to be copied.
    Click              App.JButton.copyText
    ${text}=           Get Text    App.JLabel.copiedText
    Should Be Equal    ${text}    Different than text to be copied.

Skipped Test Button Copies Text Written at Text Field to Label
    [Documentation]    This test is meant to be skipped to show how the robot works.
    [Tags]             requirement 3
    Skip If            True
    Type Text          App.JTextField.inputText    Text to be copied.
    Click              App.JButton.copyText
    ${text}=           Get Text    App.JLabel.copiedText
    Should Be Equal    ${text}    Text to be copied.
