*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    chrome
${url}    https://robotsparebinindustries.com/
${username}    maria
${password}    thoushallnotpass   

*** Test Cases ***
TestCase01
    BrowserSettings
    LoginToApplication
    VerifyLogin
    LogOutApplication
    CloseBrowserSettings

*** Keywords ***
BrowserSettings
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

LoginToApplication
    Input Text    id:username    ${username}
    Input Text    id:password    ${password}
    Click Element    xpath://button[normalize-space()='Log in']
    sleep    5 seconds

VerifyLogin
    Element Should Be Visible    Id:logout
    Set Test Message    Logged in successfully
    Log To Console    Logged in successfully


LogOutApplication
    Click Element    Id:logout
    Log To Console    Logged out successfully
    Set Test Message    Logged out successfully

CloseBrowserSettings
    close Browser
    
    