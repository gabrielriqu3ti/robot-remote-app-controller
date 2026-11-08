*** Settings ***
Library  String

*** Test Cases ***
Create A Random String
    Log to Console  We are going to generate a random string
    Generate Random String  10
    Log to Console  We finished generating a random string
