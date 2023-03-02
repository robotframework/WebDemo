*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
 Hello World
    Log To Console    Hello Robot

Login Test
    Open Browser    url=https://the-internet.herokuapp.com/login    browser=firefox
    Input Text      id=username_field     user
    Input Text      id=username_field     user

    ${variable}=    Get Location
    Log To Console     ${variable}
    Should Contain     ${variable}  localhost