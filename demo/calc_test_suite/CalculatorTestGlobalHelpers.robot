*** Settings ***
Library           SikuliXRobotLibrary
Library           String

*** Keywords ***
Click "${p_button_name}" Button
    [Documentation]    Clicks a button using the region constants in CalculatorTestConstants.robot
    Set New Search Region In Active App    ${BUTTON_${p_button_name}_REGION}
    Click Region

Click Number "${p_button}" Button
    @{numbers} =    Split String To Characters    ${p_button}
    : FOR    ${number}    IN    @{numbers}
    \    Click "${number}" Button

String "${p_string}" Only Contains Numbers
    ${ret} =    Run Keyword And Return Status
    ...    Should Match Regexp    ${p_string}    [0-9]+
    Set Test Variable    ${NUMBERS_ONLY}    ${ret}

Window "${p_window}" Should Be Open
    [Documentation]    Checks if ${p_window} has window, returns True if window is available, otherwise False.
    ${has_window} =    Run Keyword and Return Status
    ...    App Has Window    ${p_window}
    Should Be True    ${has_window}

Set Focus To "${p_window}" Window
    Wait Until Keyword Succeeds    20    5
    ...    Set Application Focus    ${p_window}

Element "${p_pattern}" Should Be Visible Before Timeout
    [Documentation]    Waits until pattern is visible before timeout value, returns an error if pattern is still not visible once timeout expires.
    Wait Until Pattern Is Visible    ${p_pattern}    ${TIMEOUT}

Set Default Pattern Library Directory
    Set Image Library    ${IMAGE_LIBRARY}

Open "${p_app_name}" Application
    Check and Open Application    ${${p_app_name}_EXECUTABLE}    ${${p_app_name}_APP_NAME}
    Wait Until Keyword Succeeds    ${TIMEOUT}    ${RETRY_INTERVAL}
    ...    Window "Calculator" Should Be Open
    #Set Focus To "Calculator" Window

Close "${p_application_name}" Application
    Close Application    ${p_application_name}

Get Text In "${p_region}" Region
    [Documentation]    Returns the text in the specified region ${p_region}
    Set New Search Region In Active App    ${${p_region}_REGION}
    ${p_text}=    Get Text In Search Region    region
    [Return]    ${p_text}

#******************************************************************************#
#                                Archive
#******************************************************************************#
Get OS Type
    ${OS_type_version} =    Get Env OS Type And Version
    ${t_OS_type} =    Set Variable If
    ...    '${OS_type_version}' == 'WINDOWS 6.1'    Win7
    ...    '${OS_type_version}' == 'WINDOWS 6.3'    Win8
    Set Test Variable    ${OS_TYPE}    ${t_OS_type}

