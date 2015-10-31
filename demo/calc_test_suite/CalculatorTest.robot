*** Settings ***
Documentation     Calculator test suite for the common operations. Does not use patterns as parameters in the keywords but uses offsets of regions instead
Library           SikuliXRobotLibrary
Resource          CalculatorTestGivenWhenThen.robot
Test Setup        Open "Calculator" Application
Test Teardown     Close "Calculator" Application
Default Tags      CalculatorTest    DemoTest
Test Template     Functionality Test

*** Test Cases ***    NUM1    OPERATION    NUM2    EXPECTED RESULT
12 + 100 = 112         12     Plus         100       112
9 + 9 = 18              9     Plus           9        18
112 - 100 = 12        112     Minus        100        12
119 - 9 = 110         119     Minus          9       110    # You may set a test case to fail in order to see how the reporting works.
100 / 2 = 50          100     Divide         2        50
1 / 4 = 0.25            1     Divide         4      0.25
10 * 100 = 1000        10     Times        100      1000
2 * 9 = 18              2     Times          9        18

*** Keywords ***
Functionality Test
    [Arguments]    ${num1}    ${operation}    ${num2}    ${expected_result}
    Given User Calculates "${num1}" "${operation}" "${num2}"
    When User Clicks "Equals" Button
    Then Actual Result Should Be Equal To "${expected_result}"
