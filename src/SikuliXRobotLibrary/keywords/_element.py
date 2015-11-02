from sikuli import *
from SikuliXRobotLibrary.locators import PatternFinder
from SikuliXRobotLibrary import utils
from keywordgroup import KeywordGroup

class _ElementKeywords(KeywordGroup):
    def __init__(self):
        self._pattern_finder = PatternFinder()

    # Public

    """***************************** MOUSE ACTIONS ************************************
    Performs mouse actions on matching pattern that will serve as locators.
    Search region or setROI() value is set to the application in focus as default.
    Locators or patterns must be any of the following format: <image.png>, <image.png> = <sensitivity from 0.00 to 0.99>, <string>
    For example:
    |  Click Pattern    pattern.png = 0.90
    |  Click Pattern    pattern.png
    |  Click Pattern    Password
    """
    
    def click_region(self):
        """Left-clicks the center x,y coordinate of a specified ROI or search region.

        This keyword must be paired with any of the following keywords:
        `Set Search Region To Target Screen`, `Set New Search Region In Active App`, 
        `Set Search Region To Application`, `Set New Search Region In Target Screen` or 
        `Set New Search Region In Application`.

        See also `Double Click Region`, `Right Click Region`, `Get Text In Search Region`, `Hover At Region`
        and `Highlight Region`.

        Example:
        | Set New Search Region In Active App | 10, 60, -20, -270 | # Sets offset values to a region of active app.            |
        | Click Region                        |                   | # Clicks the center of the specified ROI or search region. |
        """
        self._info("Clicking specified ROI or search region. Last match: '%s'" % getLastMatch())
        click()

    def double_click_region(self):
        """Double-clicks the center x,y coordinate of a specified ROI or search region.

        This keyword must be paired with any of the following keywords:
        `Set Search Region To Target Screen`, `Set New Search Region In Active App`, 
        `Set Search Region To Application`, `Set New Search Region In Target Screen` or 
        `Set New Search Region In Application`.

        See also `Click Region`, `Right Click Region`, `Get Text In Search Region`, `Hover At Region`
        and `Highlight Region`.

        Example:
        | Set New Search Region In Active App | 10, 60, -20, -270 | # Sets offset values to a region of active app.                   |
        | Double Click Region                 |                   | # Double-clicks the center of the specified ROI or search region. |
        """
        self._info("Double-clicking specified ROI or search region. Last match: '%s'" % getLastMatch())
        doubleClick()

    def right_click_region(self):
        """Right-clicks the center x,y coordinate of a specified ROI or search region.

        This keyword must be paired with any of the following keywords:
        `Set Search Region To Target Screen`, `Set New Search Region In Active App`, 
        `Set Search Region To Application`, `Set New Search Region In Target Screen` or 
        `Set New Search Region In Application`.

        See also `Click Region`, `Double Click Region`, `Get Text In Search Region`, `Hover At Region`
        and `Highlight Region`.

        Example:
        | Set New Search Region In Active App | 10, 60, -20, -270 | # Sets offset values to a region of active app.                   |
        | Right Click Region                  |                   | # Right-clicks the center of the specified ROI or search region. |
        """
        self._info("Right-clicking specified ROI or search region. Last match: '%s'" % getLastMatch())
        rightClick()

    def highlight_region(self, highlight_duration):
        """Highlights the specified ROI or search region for a specified ``highlight_duration`` in seconds.

        This keyword must be paired with any of the following keywords:
        `Set Search Region To Target Screen`, `Set New Search Region In Active App`, 
        `Set Search Region To Application`, `Set New Search Region In Target Screen` or 
        `Set New Search Region In Application`.

        See also `Click Region`, `Double Click Region`, `Right Click Region`, `Hover At Region` and `Get Text In Search Region`.

        Example:
        | Set New Search Region In Active App | 10, 60, -20, -270 | # Sets offset values to a region of active app.                 |
        | Highlight Region                    | 2                 | # Highlights the specified ROI or search region. for 2 seconds. |
        """
        self._info("Highlighting specified ROI or search region for '%s'second(s)." % (highlight_duration))
        highlight(float(highlight_duration))

    def hover_at_region(self):
        """Hovers mouse pointer at center x,y coordinate of a specified ROI or search region.

        This keyword must be paired with any of the following keywords:
        `Set Search Region To Target Screen`, `Set New Search Region In Active App`, 
        `Set Search Region To Application`, `Set New Search Region In Target Screen` or 
        `Set New Search Region In Application`.

        See also `Double Click Region`, `Right Click Region`, `Get Text In Search Region`
        and `Highlight Region`.

        Example:
        | Set New Search Region In Active App | 10, 60, -20, -270 | # Sets offset values to a region of active app. |
        | Hover At Region                     |                   | # Hovers mouse pointer at the center of specified ROI or search region. |
        """
        self._info("Hovering at specified ROI or search region. Last match: '%s'" % getLastMatch())
        hover()

    def click_pattern(self, pattern):
        """Perform a mouse `click` on the click point using the `left` button.
        Click point is at the `center` of the element identified by ``pattern``.

        Key attributes for arbitrary patterns are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.
        """
        self._info("Clicking element '%s'." % pattern)
        self._pattern_find(pattern, None, None).click()

    def click_pattern_at_coordinates(self, pattern, xoffset, yoffset):
        """Perform a mouse `click` on the click point using the `left` button.
        Click point is at `x/y` coordinates of the element identified by ``pattern``.

        Key attributes for arbitrary patterns are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.
        """
        self._info("Click element '%s' in coordinates '%s', '%s'." % (pattern, xoffset, yoffset))
        self._pattern_find(pattern, xoffset, yoffset).click()

    def right_click_pattern(self, pattern):
        """Perform a mouse `click` on the click point using the `right` button.
        Click point is at the `center` of the element identified by ``pattern``.

        Key attributes for arbitrary patterns are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.
        """
        self._info("Right-clicking element '%s'." % pattern)
        self._pattern_find(pattern, None, None).rightClick()

    def right_click_pattern_at_coordinates(self, pattern, xoffset, yoffset):
        """Perform a mouse `click` on the click point using the `right` button.
        Click point is at `x/y` coordinates of the element identified by ``pattern``.

        Key attributes for arbitrary patterns are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.
        """
        self._info("Right-clicking element '%s' in coordinates '%s', '%s'." % (pattern, xoffset, yoffset))
        self._pattern_find(pattern, xoffset, yoffset).rightClick()

    def double_click_pattern(self, pattern):
        """Perform a mouse `double-click` on the click point using the `left` button.
        Click point is at the `center` of the element identified by ``pattern``.

        Key attributes for arbitrary patterns are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.
        """
        self._info("Double-clicking element '%s'." % pattern)
        self._pattern_find(pattern, None, None).doubleClick()

    def double_click_pattern_at_coordinates(self, pattern, xoffset, yoffset):
        """Perform a mouse `double-click` on the click point using the `left` button.
        Click point is at `x/y` coordinates of the element identified by ``pattern``.

        Key attributes for arbitrary patterns are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.
        """
        self._info("Double-clicking element '%s' in coordinates '%s', '%s'." % (pattern, xoffset, yoffset))
        self._pattern_find(pattern, xoffset, yoffset).doubleClick()

    def highlight_pattern(self, pattern, highlight_duration):
        """Highlight element identified by ``pattern`` for a specified ``highlight_duration`` in seconds.

        Key attributes for arbitrary ``patterns`` are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.

        Example:
        | Highlight Pattern | pattern.png = 0.90 | 2   | This is a sample text. | # Type a text in element identified by pattern.png |
        """
        self._info("Highlighting element '%s' for '%s' second(s)." % (pattern, highlight_duration))
        self._pattern_find(pattern, None, None).highlight(float(highlight_duration))

    def hover_at_pattern(self, pattern):
        """Hover mouse pointer at center of element identified by ``pattern``.

        Key attributes for arbitrary ``patterns`` are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.
        """
        self._info("Hovering at element '%s'." % pattern)
        self._pattern_find(pattern, None, None).hover()

    def hover_at_pattern_at_coordinates(self, pattern, xoffset, yoffset):
        """Hover mouse pointer at `x/y` coordinates of the element identified by ``pattern``.

        Key attributes for arbitrary ``patterns`` are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.
        """
        self._info("Hovering at element '%s' in coordinates '%s', '%s'." % (pattern, xoffset, yoffset))
        self._pattern_find(pattern, xoffset, yoffset).hover()

    def move_mouse_at_coordinates(self, xoffset, yoffset):
        """Move mouse cursor coordinates at ``x/y`` coordinates of the `screen`.
        """
        self._info("Moving mouse at coordinates '%s', '%s'." % (xoffset, yoffset))
        mouseMove(int(xoffset), int(yoffset))

    def mouse_button_down(self, mouse_button):
        """Press the ``left`` mouse button `down`. 
        Must be paired with `Mouse Button Up` keyword.
        """
        self._info("Mouse down at, '%s' button." % (mouse_button))
        mouseDown(self._mouse_button(mouse_button))

    def mouse_button_up(self, mouse_button):
        """Release the mouse button previously pressed. 
        Must be paired with `Mouse Button Down` keyword.
        """
        self._info("Mouse up at, '%s' button." % (mouse_button))
        mouseUp(self._mouse_button(mouse_button))

    def scroll_from_pattern(self, pattern, scroll):
        """Scroll up or down as specified by the `scroll step` at center of the element identified by ``pattern``.
        Key attributes for arbitrary ``patterns`` are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.

        Examples:
        | Scroll From Pattern | Up = 10   | # Scroll up 10 steps. |
        | Scroll From Pattern | Down = 10 | # Scroll down 10 steps. |
        """
        self.hover_at_pattern(pattern)
        self._info("Scrolling '%s' in pattern '%s'." % (scroll, pattern))
        self._scroll_direction_and_steps_from_pattern(pattern, scroll, None, None)

    def scroll_from_pattern_at_coordinates(self, pattern, scroll, xoffset, yoffset):
        """Scroll up or down as specified by the `scroll` step at `x/y` coordinates of the element identified by ``pattern``.

        Key attributes for arbitrary ``patterns`` are `images` which is advisably in PNG format or `strings`. 
        See `introduction` for details about locating elements.
        
        Examples:
        | Scroll From Pattern At Coordinates | pattern.png = 0.80 | Up = 10   | # Scroll up 10 steps.   |
        | Scroll From Pattern At Coordinates | pattern.png = 0.80 |  Down = 10 | # Scroll down 10 steps. |
        """
        self.hover_at_pattern_at_coordinates(pattern, xoffset, yoffset)
        self._info("Scrolling '%s' in pattern '%s'  at coordinates '%s', '%s'." % (scroll, pattern, xoffset, yoffset))
        self._scroll_direction_and_steps_from_pattern(pattern, scroll, xoffset, yoffset)

    def scroll_x_steps(self, scroll):
        """Scroll up or down as specified by the `scroll` step.

        This keyword must be paired with `Hover At Pattern` in order to execute scrolling action within the region.
        Examples:
        | Hover At Pattern | pattern.png | # Hover at element identified by pattern.png |
        | Scroll X Steps   | Up = 10     | # Scroll up 10 steps.                        |
        | Scroll X Steps   | Down = 10   | # Scroll down 10 steps.                      |
        """
        self._info("Scrolling '%s'." % (scroll))
        self._scroll_direction_and_steps(scroll)

    """************************** MOUSE ACTIONS DRAG AND DROP *****************************"""
    def drag_pattern(self, pattern):
        """`Drag Pattern` and `Drop At Pattern` keywords must be used in pairs to complete a drag and drop action.

        Examples:
        | Drag Pattern    | pattern.png = 0.90 | # Drag element identified by pattern.png    |
        | Drop At Pattern | pattern.png = 0.90 | # Drag at element identified by pattern.png |
        """
        self._info("Dragging element '%s'." % pattern)
        drag(self._pattern_find(pattern, None, None))

    def drop_at_pattern(self, pattern):
        """`Drag Pattern` and `Drop At Pattern` keywords must be used in pairs to complete a drag and drop action.

        Examples:
        | Drag Pattern    | pattern.png | # Drag element identified by pattern.png    |
        | Drop At Pattern | pattern.png | # Drag at element identified by pattern.png |
        """
        self._info("Dropping at element '%s'." % pattern)
        dropAt(self._pattern_find(pattern, None, None))

    def drag_pattern_in_coordinates(self, pattern, xoffset, yoffset):
        """Drag element at `x/y` coordinates of the element identified by ``pattern``.
        """
        self._info("Dragging element '%s' in coordinates '%s', '%s'." % (pattern, xoffset, yoffset))
        drag(self._pattern_find(pattern, xoffset, yoffset))

    def drop_pattern_at_coordinates(self, pattern, xoffset, yoffset):
        """Drop or release mouse button element at `x/y` coordinates of the element identified by ``pattern``.
        """
        self._info("Dropping element '%s' in coordinates '%s', '%s'." % (pattern, xoffset, yoffset))
        dropAt(self._pattern_find(pattern, xoffset, yoffset))

    def drag_and_drop_element(self, pattern1, pattern2):
        """Drag and drop an element identified by ``pattern1`` to another element identified by ``pattern2``.

        Example:
        | Drag and drop | pattern1.png = 0.90 | pattern2.png = 0.90 | # Drag element identified by pattern.png |
        """
        self._info("Performing drag and drop from element '%s' to element '%s'." % (pattern1, pattern2))
        dragDrop(self._pattern_find(pattern1, None, None), self._pattern_find(pattern2, None, None))

    """***************************** KEYBOARD ACTIONS ************************************"""
    def paste_text_in_pattern(self, pattern, text):
        """Paste a `text` in element identified by ``pattern``.

        Example:
        | Paste Text In Pattern | pattern.png = 0.90 | This is a sample text. | # Paste a text in element identified by pattern.png |
        """
        text = str(text)
        self._info("Pasting text '%s' in pattern '%s'." % (text, pattern))
        self._pattern_find(pattern, None, None).paste(text)

    def paste_text_in_pattern_at_coordinates(self, pattern, text, xoffset, yoffset):

        """Paste a `text` at `x/y` coordinates of the element identified by ``pattern``.
        Example:
        | Paste Text In Pattern | pattern.png = 0.90 | 30 | 30 | This is a sample text. | # Paste a text in x/y coordinates of element identified by pattern.png |
        """
        self._info("Pasting text '%s' in '%s'  at coordinates '%s', '%s'." % (text, pattern, xoffset, yoffset))
        self._pattern_find(pattern, xoffset, yoffset).paste(text)

    def type_text_in_pattern(self, pattern, text):
        """Type a `text` in element identified by ``pattern``.

        Example:
        | Type Text In Pattern | pattern.png = 0.90 | This is a sample text. | # Type a text in element identified by pattern.png |
        """
        text = str(text)
        self._info("Typing '%s' in pattern '%s'." % (text, pattern))
        self._pattern_find(pattern, None, None).type(text)

    def type_text_in_pattern_at_coordinates(self, pattern, text, xoffset, yoffset):
        """Paste a `text` at `x/y` coordinates of the element identified by ``pattern``.

        Example:
        | Type Text In Pattern | pattern.png = 0.90 | 30 | 30 | This is a sample text. | # Type a text in x/y coordinates of element identified by pattern.png |
        """
        self._info("Typing text '%s' in '%s'  at coordinates '%s', '%s'." % (text, pattern, xoffset, yoffset))
        self._pattern_find(pattern, xoffset, yoffset).type(text)

    """***************************** READ TEXTS IN PATTERN ************************************
    Note: OCR tessdata should downloaded then put in a local directory
    For Windows, it should be put inside C:\Users\<user>\AppData\Roaming\Sikulix\SikulixTesseract
    Or: User must select the last two options in the SikuliX installation to install both the script and tesseract.
    """

    def get_text_in_pattern(self, pattern, search_location):
        """Returns the text in an ``area`` at a ``spatial location`` in reference to an element identified by ``pattern``

        Examples:
        | Get Text In Pattern | pattern.png | None        | # Returns the text within 300px left of element identified by pattern.png  |
        | Get Text In Pattern | pattern.png | left = 300  | # Returns the text within 300px left of element identified by pattern.png  |
        | Get Text In Pattern | pattern.png | right = 400 | # Returns the text within 400px right of element identified by pattern.png |
        | Get Text In Pattern | pattern.png | above = 500 | # Returns the text within 500px above of element identified by pattern.png |
        | Get Text In Pattern | pattern.png | below = 600 | # Returns the text within 600px below of element identified by pattern.png |
        """
        self._info("Getting texts in pattern at '%s' of pattern '%s'." % (search_location, pattern))
        return self._read_text_in_pattern(pattern, search_location)

    def get_text_in_search_region(self, search_location):
        """Returns the text from a specified ``search location``. 

        This keyword must be paired with any of the following keywords:
        `Set Search Region To Target Screen`, `Set New Search Region In Active App`, 
        `Set Search Region To Application`, `Set New Search Region In Target Screen` or 
        `Set New Search Region In Application`.

        See also `Click Region`, `Double Click Region`, `Right Click Region`,
        and `Highlight Region`.

        Examples:
        | Set New Search Region In Active App | 10, 60, -20, -270 | # Sets offset values to a region of active app.        |
        | Get Text In Search Region           | region            | # Returns the text within the specified search region. |
        | Get Text In Search Region           | left 300          | # Returns the text within the specified search region. |
        | Get Text In Search Region           | right 400         | # Returns the text within the specified search region. |
        | Get Text In Search Region           | above 500         | # Returns the text within the specified search region. |
        """
        self._info("Getting texts from at '%s' of specified ROI." % (search_location))
        return self._read_text_in_region(search_location)

    """***************************** DO SOMETHING IN MATCHING PATTERNS IN ACTIVE WINDOW ************************************
    Keywords used when multiple patterns on screen is present.
    Search region or setROI() value is set to the application in focus as default.
    Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
    """

    def get_pattern_count_in_active_app(self, pattern):
        """Returns the count of elements identified by ``pattern`` in the region of an active application.

        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.
        """
        self._info("Getting count of pattern '%s' in active app." % pattern)
        return len(self._get_all_patterns_in_active_app(pattern))

    def click_nth_pattern_in_active_app(self, pattern, pattern_index):
        """Perform a mouse ``click`` on the click point using the ``left`` button.

        Click point is at the `center` of the nth element identified by ``pattern``.
        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at maximum level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Example:
        | Click Nth Pattern In Active App | pattern.png = 0.99 | 3 | # Clicks the third instance of an element identified by pattern.png |
        """
        self._info("Clicking '%s'nth pattern '%s' in active app." % (pattern_index, pattern))
        self._get_nth_pattern(pattern, pattern_index).click()

    def right_click_nth_pattern_in_active_app(self, pattern, pattern_index):
        """Perform a mouse ``click`` on the click point using the ``right`` button.

        Click point is at the `center` of the nth element identified by ``pattern``.
        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Example:
        | Right Click Nth Pattern In Active App | pattern.png = 0.99 | 4 | # Right-clicks the fourth instance of an element identified by pattern.png |
        """
        self._info("Clicking '%s'nth pattern '%s' in active app." % (pattern_index, pattern))
        self._get_nth_pattern(pattern, pattern_index).rightClick()

    def double_click_nth_pattern_in_active_app(self, pattern, pattern_index):
        """Perform a mouse ``double-click`` on the click point using the ``left`` button.

        Click point is at the `center` of the nth element identified by ``pattern``.
        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Example:
        | Double Click Nth Pattern In Active App | pattern.png = 0.99 | 5 | # Double-clicks the fifth instance of an element identified by pattern.png |
        """

        self._info("Double-clicking '%s'nth pattern '%s' in active app." % (pattern_index, pattern))
        self._get_nth_pattern(pattern, pattern_index).doubleClick()

    def hover_at_nth_pattern_in_active_app(self, pattern, pattern_index):
        """Hovers mouse pointer at the center the nth element identified by ``pattern``.

        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Example:
        | Hover At Nth Pattern In Active App | pattern.png = 0.99 | 7 | # Hovers mouse pointer the seventh instance of an element identified by pattern.png |
        """

        self._info("Hovering at '%s'nth pattern '%s' in active app." % (pattern_index, pattern))
        self._get_nth_pattern(pattern, pattern_index).hover()

    def highlight_nth_pattern_in_active_app(self, pattern, pattern_index, highlight_duration):
        """Highlights the nth element identified by ``pattern`` for a specified `highlight_duration` in seconds.

        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Example:
        | Highlight Nth Pattern In Active App | pattern.png = 0.99 | 6   | 2   | 
        # Highlights the sixth instance of an element identified by pattern.png for 2 seconds.
       
        """

        self._info("Highlighting '%s'nth pattern '%s' in active app for '%s' second(s)." % (pattern_index, pattern, highlight_duration))
        self._get_nth_pattern(pattern, pattern_index).highlight(float(highlight_duration))

    def drag_nth_pattern_in_active_app(self, pattern, pattern_index):
        """Drag the nth element identified by ``pattern``.
        `Drag Nth Pattern In Active App` and `Drop At Nth Pattern In Active App` keywords must be used in pairs to complete a drag and drop action.

        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Examples:
        | Drag Nth Pattern In Active App    | pattern.png = 0.99 | 1  | # Drags the first instance of an element identified by pattern.png   |
        | Drop At Nth Pattern In Active App | pattern.png = 0.99 | 13 | # Drops at the 13th instance of an element identified by pattern.png |
        """

        self._info("Dragging '%s'nth pattern '%s' in active app." % (pattern_index, pattern))
        drag(self._get_nth_pattern(pattern, pattern_index))

    def drop_at_nth_pattern_in_active_app(self, pattern, pattern_index):
        """Drop at the nth element identified by ``pattern``.
        `Drag Nth Pattern In Active App` and `Drop At Nth Pattern In Active App` keywords must be used in pairs to complete a drag and drop action.

        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Examples:
        | Drag Nth Pattern In Active App    | pattern.png = 0.99 | 13  | # Drags the 13th instance of an element identified by pattern.png   |
        | Drop At Nth Pattern In Active App | pattern.png = 0.99 | 1 | # Drops at the first instance of an element identified by pattern.png |
        """

        self._info("Dropping at '%s'nth pattern '%s' in active app." % (pattern_index, pattern))
        dropAt(self._get_nth_pattern(pattern, pattern_index))

    def drag_and_drop_from_nth_pattern(self, pattern1, pattern1_index, pattern2, pattern2_index):
        """Drag and drop an nth element identified by ``pattern1`` to another nth element identified by ``pattern2``.

        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Examples:
        | Drag and drop | pattern1.png = 0.90 | 1 | pattern2.png = 0.90 | 2 | # Drag and drop the first instance of pattern1.png to the 2nd instance of pattern2.png |
        | Drag and drop | pattern.png = 0.90  | 3 | pattern.png = 0.90  | 4 | # Drag and drop the third instance to the fourth instance of pattern.png |
        """

        self._info("Performing drag and drop from element '%s' to element '%s'." % (pattern1, pattern2))
        dragDrop(self._get_nth_pattern(pattern1, pattern1_index),
                 self._get_nth_pattern(pattern2, pattern2_index))

    def paste_text_in_nth_pattern_in_active_app(self, pattern, pattern_index, text):
        """Paste a `text` at `x/y` coordinates of the element identified by ``pattern``.

        Example:
        | Type Text In Pattern | pattern.png = 0.90 | This is a sample text. | # Type a text in element identified by pattern.png |
        """

        self._info("Pasting text '%s' in '%s'nth pattern '%s' in active app." % (text, pattern_index, pattern))
        self._get_nth_pattern(pattern, pattern_index).type(text)

    def type_text_in_nth_pattern_in_active_app(self, pattern, pattern_index, text):
        """Type a `text` in nth element identified by ``pattern``.

        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Example:
        | Type Text At Nth Pattern In Active App | pattern.png = 0.90 | 3 | This is a sample text. | # Type a text in third element identified by pattern.png |
        """

        self._info("Typing text '%s' in '%s'nth pattern '%s' in active app." % (text, pattern_index, pattern))
        self._get_nth_pattern(pattern, pattern_index).type(text)

    def get_text_in_nth_pattern(self, pattern, pattern_index, search_location):
        """Return the `text` in nth element identified by ``pattern``.

        This Keyword is useful when multiple patterns on screen is present.
        Search region or setROI() value is set to the application in focus as default.
        Pattern sensitivity must be set at max level (0.99) in order to avoid false positives during image detections.
        Search for matching patterns is set to top > down > left > right.

        Examples:
        | Get Text In Nth Pattern At Location And Area | pattern.png | 1 | None        | # Returns the text of the first instance of pattern.png                     |
        | Get Text In Nth Pattern At Location And Area | pattern.png | 1 | left = 300  | # Returns the text within 300px left of the first instance of pattern.png   |
        | Get Text In Nth Pattern At Location And Area | pattern.png | 2 | right = 400 | # Returns the text within 400px right of the second instance of pattern.png |
        | Get Text In Nth Pattern At Location And Area | pattern.png | 3 | above = 500 | # Returns the text within 500px above of the third instance of pattern.png  |
        | Get Text In Nth Pattern At Location And Area | pattern.png | 5 | below = 600 | # Returns the text within 600px below of the fifth instance of pattern.png  |
        """

        self._info("Getting texts in '%s' nth pattern at '%s' of pattern '%s'." % (pattern_index, search_location, pattern))
        pattern = self._get_nth_pattern(pattern, pattern_index)
        return self._read_text(pattern, search_location)

    # Private
    """***************************** Internal methods ************************************"""
    def _pattern_find(self, pattern, xoffset, yoffset):
        """Finds ``pattern`` on search region set by active application.
        To do: dynamic search region where user can set the search region to either, active application, specific region or screen
        """

        active_app_window = App.focusedWindow();
        app_coordinates = (active_app_window.getX(), active_app_window.getY(), active_app_window.getW(), active_app_window.getH())
        setROI(*app_coordinates)
        matching_pattern = self._pattern_finder._find_pattern(pattern)
        try:
            if (xoffset != None or yoffset != None):
                xoffset = int(xoffset); yoffset = int(yoffset)
                element = active_app_window.find(matching_pattern.targetOffset(xoffset, yoffset))
            else:
                element = active_app_window.find(matching_pattern)
            return element
        except FindFailed, err:
            raise AssertionError("No matching pattern: %s found on screen." % (pattern))

    def _scroll_direction_and_steps(self, scroll):
        (scroll_direction, scroll_steps) = self._pattern_finder._parse_scroll_details(scroll)
        if (scroll_direction == "up"):
            scroll_direction = WHEEL_UP
        elif (scroll_direction == "down"):
            scroll_direction = WHEEL_DOWN
        return wheel(scroll_direction, scroll_steps)

    def _scroll_direction_and_steps_from_pattern(self, pattern, scroll, xoffset, yoffset):
        (scroll_direction, scroll_steps) = self._pattern_finder._parse_scroll_details(scroll)
        if (scroll_direction == "up"):
            scroll_direction = WHEEL_UP
        elif (scroll_direction == "down"):
            scroll_direction = WHEEL_DOWN
        return self._pattern_find(pattern, xoffset, yoffset).wheel(scroll_direction, scroll_steps)

    def _read_text_in_pattern(self, pattern, search_location):
        (location, search_area) = self._parse_spatial_location(search_location)
        pattern = self._pattern_find(pattern, None, None)
        if (location == "left"):
            pattern_text = pattern.left(search_area).text()
        elif (location == "right"):
            pattern_text = pattern.right(search_area).text()
        elif (location == "above"):
            pattern_text = pattern.above(search_area).text()
        elif (location == "below"):
            pattern_text = pattern.below(search_area).text()
        else:
            pattern_text = pattern.text()
        return pattern_text

    def _read_text_in_region(self, search_location):
        (location, search_area) = self._parse_spatial_location(search_location)
        if (location == "left"):
            region_text = left(search_area).text()
        elif (location == "right"):
            region_text = right(search_area).text()
        elif (location == "above"):
            region_text = above(search_area).text()
        elif (location == "below"):
            region_text = below(search_area).text()
        else:
            region_text = text()
        return region_text

    def _parse_spatial_location(self, search_location):
        assert search_location is not None and len(search_location) > 0
        search_location = search_location.lower()
        
        if (search_location == "region") :
            location = None
            search_area = None
        else:
            search_location = search_location.partition('=')
            location = search_location[0].strip()
            search_area = int(search_location[2].strip())
        return (location, search_area)

    def _mouse_button(self, mouse_button):
        assert mouse_button is not None and len(mouse_button) > 0
        mouse_button = mouse_button.lower()
        if(mouse_button == "left"):
            mouse_button = Button.LEFT
        elif(mouse_button == "middle"):
            mouse_button = Button.MIDDLE
        elif(mouse_button == "right"):
            mouse_button = Button.RIGHT
        return mouse_button

    def _set_image_order(self, match):
        return match.x, match.y

    def _get_all_patterns_in_active_app(self, pattern):
        self.set_search_region_to_active_app()
        active_app_region = Region(*self.get_active_app_coordinates())
        list_of_patterns = []; sorted_patterns = []
        try:
            found_patterns =  active_app_region.findAll(self._pattern_finder._find_pattern(pattern))
            while found_patterns.hasNext():
                list_of_patterns.append(found_patterns.next())
            sorted_patterns = sorted(list_of_patterns, key=self._set_image_order)
            return sorted_patterns
        except FindFailed, err:
            AssertionError("No matching pattern(s): %s found on screen." % (pattern))

    def _get_nth_pattern(self, pattern, pattern_index):
        pattern_index = int(pattern_index) - 1
        nth_pattern = self._get_all_patterns_in_active_app(pattern)[pattern_index]
        return nth_pattern