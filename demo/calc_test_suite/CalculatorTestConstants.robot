*** Variables ***

#******************************************************************************#
#                             PATTERN LIBRARY
#******************************************************************************#
${WIN7_CALCULATOR_APP}           Win7/calc.png
${WIN8_CALCULATOR_APP}           Win8/calc.png

#******************************************************************************#
#                           Offsets: x, y, width, height
#******************************************************************************#
#[Documentation]    These constants uses regions instead of patterns, thus leads to a smaller storage cost
${BUTTON_0_REGION}                    18, 276, -157, -296
${BUTTON_1_REGION}                    18, 244, -195, -296
${BUTTON_2_REGION}                    58, 244, -195, -296
${BUTTON_3_REGION}                    98, 244, -195, -296
${BUTTON_4_REGION}                    18, 212, -195, -296
${BUTTON_5_REGION}                    58, 212, -195, -296
${BUTTON_6_REGION}                    98, 212, -195, -296
${BUTTON_7_REGION}                    18, 180, -195, -296
${BUTTON_8_REGION}                    58, 180, -195, -296
${BUTTON_9_REGION}                    98, 180, -195, -296
${BUTTON_DECIMAL_REGION}              98, 276, -195, -296
${BUTTON_PLUS_REGION}                 136, 276, -195, -296
${BUTTON_MINUS_REGION}                136, 244, -195, -296
${BUTTON_TIMES_REGION}                136, 212, -195, -296
${BUTTON_DIVIDE_REGION}               136, 180, -195, -296
${BUTTON_EQUALS_REGION}               176, 244, -195, -265
${CALCULATOR_RESULT_SCREEN_REGION}    18, 61, -40, -274

#******************************************************************************#
#                             File Path/Directories
#******************************************************************************#
${IMAGE_LIBRARY}                  ${CURDIR}\\calc_image_library
${CALCULATOR_EXECUTABLE}          C:/Windows/System32/calc.exe
${CALCULATOR_APP_NAME}            Calculator

#******************************************************************************#
#                             Timeouts and Retries
#******************************************************************************#
${TIMEOUT}                        20
${RETRY_INTERVAL}                 5