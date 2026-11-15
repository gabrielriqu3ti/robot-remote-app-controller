*** Settings ***
Documentation    A test suite to test a remote controlled app.
Resource         resources/remotecontrolledapp.resource
Test Setup       Connect to App
Test Teardown    Disconnect from App
Test Tags        PV.001    positive


*** Test Cases ***
Test Text Field Can Be Written
    [Tags]             TEST-001    ET.001-001
    ${text}=           Type Text    App.JTextField.inputText    Text typed into Text Field.
    Should Be Equal    ${text}    Text typed into Text Field.

Test Button Can Be Clicked
    [Tags]             TEST-002    ET.001-002
    Click              App.JButton.copyText

Test Button Copies Text Written at Text Field to Label
    [Tags]             TEST-003    ET.001-003
    Type Text          App.JTextField.inputText    Insert text here...
    Take Screenshot    app_before_robot.png
    Type Text          App.JTextField.inputText    Text to be copied.
    Click              App.JButton.copyText
    ${text}=           Get Text    App.JLabel.copiedText
    Take Screenshot    app_after_robot.png
    Should Be Equal    ${text}    Text to be copied.

Failed Test Button Copies Text Written at Text Field to Label
    [Documentation]    This test is meant to fail to show how the robot works.
    [Tags]             TEST-004    ET.001-003    -positive    negative
    Type Text          App.JTextField.inputText    Text to be copied.
    Take Screenshot    app_before_failed_test_robot.png
    Click              App.JButton.copyText
    ${text}=           Get Text    App.JLabel.copiedText
    Take Screenshot    app_after_failed_test_robot.png
    Should Be Equal    ${text}    Different than text to be copied.

Skipped Test Button Copies Text Written at Text Field to Label
    [Documentation]    This test is meant to be skipped to show how the robot works.
    [Tags]             TEST-005    ET.001-003
    Skip If            True
    Type Text          App.JTextField.inputText    Text to be copied.
    Click              App.JButton.copyText
    ${text}=           Get Text    App.JLabel.copiedText
    Should Be Equal    ${text}    Text to be copied.

Manual Test Button Copies Text Written at Text Field to Label
    [Documentation]    This test is meant to be skipped since it is a manual test.
    [Tags]             TEST-006    ET.001-003    manual
    [Setup]            NONE
    Skip
    Manual Action      Type Text    App.JTextField.inputText    Text to be copied.
    Manual Action      Click    App.JButton.copyText
    Manual Action      ${text}=    Get Text    App.JLabel.copiedText
    Manual Action      Should Be Equal    ${text}    Text to be copied.\n
    [Teardown]         NONE
