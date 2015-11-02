from sikuli import *
from keywordgroup import KeywordGroup

class _KeyboardActionsKeywords(KeywordGroup):

    # Public

    """***************************** KEYBOARD ACTIONS ************************************
    Keyword to implement pressing keyboard keys.
    Note: If the key is not in the map of supported keyboard keys, the specified string or character
    is typed instead as a string or character respectively.
    """

    def press_keyboard_key(self, keyboard_keys):
        """ Simulates pressing `keyboard keys`.
        Single key; 
        2-key combination example: Ctrl + Shift; 
        3-key combination example: Ctrl + Shift + Delete

        Examples:
        | Press Keyboard Key | DELETE                | # Presses the Delete button           |
        | Press Keyboard Key | CTRL + A              | # Presses the keys Ctrl + A              |
        | Press Keyboard Key | CTRL + Shift          | # Presses the keys Ctrl + Shift          |
        | Press Keyboard Key | CTRL + Shift + Delete | # Presses the keys Ctrl + Shift + Delete |
        """
        (keys, len_keys) =self._split_and_map_keys(keyboard_keys)
        try:
            if (len_keys == 1):
                type(keys[0])
            elif (len_keys == 2):
                type(keys[1], keys[0])
            elif (len_keys == 3):
                type(keys[2], keys[0] + keys[1])
        except ValueError:
            raise ValueError("Unsupported keys '%s'." % (keys))

    def press_key_n_times(self, keyboard_key, count):
        """ Simulates pressing a `key` multiple times as specified by count value

        Examples:
        | Press Key N Times | BACKSPACE | 5 | # Press Backspace key five times |
        | Press Key N Times | A         | 8 | # Press A eight times |
        """
        count = int(count)
        keyboard_key = self._map_supported_keyboard_keys(keyboard_key)
        type(keyboard_key * count)

    def type_string(self, string_param):
        """ Types a string as specified by `srtring_param`

        See also `Paste String`.

        Example:
        | Type String | A quick cat fox jumps over the mat. | # Types the specified string |
        """
        string_param = string_param.strip()
        type(string_param)

    def paste_string(self, string_param):
        """ Pastes a string as specified by `srtring_param`

        See also `Type String`.

        Example:
        | Paste String | A quick cat fox jumps over the mat. | # Types the specified string |
        """
        string_param = string_param.strip()
        paste(string_param)

    # Private
    """***************************** INTERNAL METHODS ************************************"""
    def _clean_string(self, string_param):
        string_param = str(string_param)
        assert string_param is not None and len(string_param) > 0
        string_param = string_param.strip()
        return string_param

    def _split_and_map_keys(self, keyboard_keys):      
        keyboard_keys = self._clean_string(keyboard_keys)
        keyboard_keys = keyboard_keys.split(' + ')
        mapped_keys = []
        for key in keyboard_keys:
            mapped_keys.append(self._map_supported_keyboard_keys(key))
        len_mapped_keys = len(mapped_keys)
        return mapped_keys, len_mapped_keys

    def _map_supported_keyboard_keys(self, keyboard_key):
        assert keyboard_key is not None and len(keyboard_key) > 0
        map = {
            "WIN": Key.WIN,
            "ENTER": Key.ENTER,
            "ALT": Key.ALT,
            "CMD": Key.CMD,
            "CTRL": Key.CTRL,
            "META": Key.META,
            "SHIFT": Key.SHIFT,
            "ALTGR": Key.ALTGR,
            "TAB": Key.TAB,
            "ESC": Key.ESC,
            "SPACE": Key.SPACE,
            "UP": Key.UP,
            "DOWN": Key.DOWN,
            "LEFT": Key.LEFT,
            "RIGHT": Key.RIGHT,
            "DELETE": Key.DELETE,
            "BACKSPACE": Key.BACKSPACE,
            "INSERT": Key.INSERT,
            "PAGE_UP": Key.PAGE_UP,
            "PAGE_DOWN": Key.PAGE_DOWN,
            "HOME": Key.HOME,
            "END": Key.END,
            "PRINTSCREEN": Key.PRINTSCREEN,
            "PAUSE": Key.PAUSE,
            "CAPS_LOCK": Key.CAPS_LOCK,
            "SCROLL_LOCK": Key.SCROLL_LOCK,
            "NUM_LOCK": Key.NUM_LOCK,
            "NUM0": Key.NUM0,
            "NUM1": Key.NUM1,
            "NUM2": Key.NUM2,
            "NUM3": Key.NUM3,
            "NUM4": Key.NUM4,
            "NUM5": Key.NUM5,
            "NUM6": Key.NUM6,
            "NUM7": Key.NUM7,
            "NUM8": Key.NUM8,
            "NUM9": Key.NUM9,
            "SEPARATOR": Key.SEPARATOR,
            "ADD": Key.ADD,
            "MINUS": Key.MINUS,
            "MULTIPLY": Key.MULTIPLY,
            "DIVIDE": Key.DIVIDE,
            "F1": Key.F1,
            "F2": Key.F2,
            "F3": Key.F3,
            "F4": Key.F4,
            "F5": Key.F5,
            "F6": Key.F6,
            "F7": Key.F7,
            "F8": Key.F8,
            "F9": Key.F9,
            "F10": Key.F10,
            "F11": Key.F11,
            "F12": Key.F12
        }
        key = map.get(keyboard_key)
        if key is None:
            return keyboard_key
        return key