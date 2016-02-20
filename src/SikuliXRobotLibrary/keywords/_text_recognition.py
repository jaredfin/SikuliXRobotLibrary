from org.sikuli.natives import OCR
from org.sikuli.script import TextRecognizer
from keywordgroup import KeywordGroup

class _TextRecognitionKeywords(KeywordGroup):

    # Public
    def set_OCR_Parameter_Whitelist(self, ocr_parameter):
        """Switches the on screen character recognition to numbers only.

        Example:
        | Set OCR Parameter Whitelist | numeric       | # Sets the On screen Character Recognition Setting To Numbers Only.                                                            |
        | Set OCR Parameter Whitelist | alpha_lower   | # Sets the On screen Character Recognition Setting To Lowercased Alpha Characters Only.                                        |
        | Set OCR Parameter Whitelist | alpha_upper   | # Sets the On screen Character Recognition Setting To Uppercased Alpha Characters Only.                                        |
        | Set OCR Parameter Whitelist | alpha         | # Sets the On screen Character Recognition Setting To Both Upper and Lower cased Alpha Characters.                             |
        | Set OCR Parameter Whitelist | alphanumeric  | # Sets the On screen Character Recognition Setting To Both Upper and Lower cased Alpha Characters And Numeric Characters Only. |
        | Set OCR Parameter Whitelist | 0123456789_.: | # Sets the On screen Character Recognition Setting To The Specified Set Of Characters                                          |
        """
        self._info("Setting OCR Text Recognition To A Specified Parameter.")
        self._set_ocr_parameter(ocr_parameter)

    def reset_text_recognizer(self):
        """Resets the text recognizer settings to default. 

        Example:
        | Switch OCR To Numbers Only | # Sets the On screen Character Recognition To Numbers Only.               |
        | Reset Text Recognizer      | # Reset the text recognizer back to the alpha-numeric text recognition.   |
        """
        
        self._info("Setting the text recognition setting to the default settings.")
        TextRecognizer.reset()
        TextRecognizer.getInstance()

    # Private
    """***************************** Internal methods ************************************"""
    def _set_ocr_parameter(self, ocr_parameter):
        """Sets ocr parameter to either, numeric, alpha or alphanumeric"""
        assert ocr_parameter is not None and len(ocr_parameter) > 0
        numeric = "0123456789"
        alpha_lower = "abcdefghijklmnopqrstuvwxyz"
        alpha_upper = alpha_lower.upper()
        alpha = alpha_lower+alpha_upper
        alphanumeric = alpha+numeric

        if (ocr_parameter == "numeric"):
            ocr_whitelist = numeric
        elif(ocr_parameter == "alpha_lower"):
            ocr_whitelist = alpha_lower
        elif(ocr_parameter == "alpha_upper"):
            ocr_whitelist = alpha_upper
        elif(ocr_parameter == "alphanumeric"):
            ocr_whitelist = alphanumeric
        else:
            ocr_whitelist = ocr_parameter

        OCR.setParameter("tessedit_char_whitelist", ocr_whitelist)