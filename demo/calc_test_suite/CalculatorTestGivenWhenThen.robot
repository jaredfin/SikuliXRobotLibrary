*** Settings ***
Resource          CalculatorTestConstants.robot
Resource          CalculatorTestGlobalHelpers.robot


*** Keywords ***
#******************************************************************************#
#                                Given
#******************************************************************************#
User Calculates "${p_num1}" "${p_operation}" "${p_num2}"
    User Clicks "${p_num1}" Button
    User Clicks "${p_operation}" Button
    User Clicks "${p_num2}" Button

User Opens "${p_application}" Application
    Open "${p_application}" Application

#******************************************************************************#
#                                When
#******************************************************************************#
User Clicks "${p_button}" Button
    String "${p_button}" Only Contains Numbers

    Run Keyword If    ${NUMBERS_ONLY}
    ...    Click Number "${p_button}" Button
    ...    ELSE
    ...    Click "${p_button}" Button

#******************************************************************************#
#                                Then
#******************************************************************************#
Actual Result Should Be Equal To "${p_expected_result}"
    ${ACTUAL_ANSWER}=    Get Text In "Calculator Result Screen" Region
    Should Be Equal    ${ACTUAL_ANSWER}    ${p_expected_result}

"${p_application}" Application Window Should Be Displayed
    Get OS Type

    Wait Until Keyword Succeeds    ${TIMEOUT}    ${RETRY_INTERVAL}
    ...    Window "${p_application}" Should Be Open

    Element "${${OS_TYPE}_${p_application}_APP}" Should Be Visible Before Timeout


#******************************************************************************#
#                            Internal Keywords
#******************************************************************************#
