*** Settings ***
Documentation     Calculator test for image assertion.
Resource          CalculatorTestGivenWhenThen.robot
Suite Setup       Set Default Pattern Library Directory
Test Teardown     Close "Calculator" Application
Default Tags      CalculatorImageAssertionTest    DemoTest2

*** Test Cases ***
Availability Test
    Given User Opens "Calculator" Application
    Then "Calculator" Application Window Should Be Displayed
