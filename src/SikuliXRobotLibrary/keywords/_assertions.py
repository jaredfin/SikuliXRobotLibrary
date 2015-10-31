from sikuli import *
from SikuliXRobotLibrary.locators import PatternFinder
from SikuliXRobotLibrary import utils
from keywordgroup import KeywordGroup

class _AssertionKeywords(KeywordGroup):

    def __init__(self):
        self._pattern_finder = PatternFinder()

    # Public
    
    def assert_pattern_is_visible_in_active_app(self, pattern):
        """Assert that ``pattern`` is visible in search region
        See `introduction` for details about locating elements.

        Note this keyword automatically searches on region of the app in focus and may be paired with the
        keyword Set Application Focus.

        See also `Assert Pattern Is Not Visible In Active App`, `Assert Pattern Is Not Visible In Region`, 
        and `Assert Pattern Is Visible In Region`.

        Example:
        | Set Application Focus                   | Calculator       |
        | Assert Pattern Is Visible in Active App | equalsbutton.png |
        # Asserts that pattern is visible in the new search region in active app as defined by offset values.
        """
        self._info("Asserting that pattern, '%s' is visible in app." % (pattern))
        self.set_search_region_to_active_app()
        try:
            assert exists(self._pattern_finder._find_pattern(pattern))
        except AssertionError, err:
            raise AssertionError("No matching pattern: %s found in search region." % (pattern))

    def assert_pattern_is_visible_in_region(self, pattern):
        """Assert that ``pattern`` is visible in search region
        See `introduction` for details about locating elements.
        
        This keyword must be paired with any of the following keywords:
        `Set Search Region To Target Screen`, `Set New Search Region In Active App`, 
        `Set Search Region To Application`, `Set New Search Region In Target Screen` or 
        `Set New Search Region In Application`.

        See also `Assert Pattern Is Not Visible In Active App`, `Assert Pattern Is Not Visible In Region`, 
        and `Assert Pattern Is Visible In Active App`.

        Example 1:
        | Set New Search Region In Active App | 10, 60, -20, -270 |
        | Assert Pattern Is Visible in Region | pattern.png       |
        # Asserts that pattern is visible in the new search region in active app as defined by offset values.

        Example 2:
        | Set New Search Region In Active Screen | 10, 60, -20, -270 |
        | Assert Pattern Is Visible in Region | pattern.png       |
        # Asserts that pattern is visible in the new search region in active screen as defined by offset values.
        """
        self._info("Asserting that pattern, '%s' is visible in specified ROI or search region." % (pattern))
        try:
            assert exists(self._pattern_finder._find_pattern(pattern))
        except AssertionError, err:
            raise AssertionError("No matching pattern: %s found in search region." % (pattern))

    def assert_pattern_is_not_visible_in_active_app(self, pattern):
        """Assert that ``pattern`` is not visible in active app.
        See `introduction` for details about locating elements.

        Note this keyword automatically searches on region of the app in focus and may be paired with the
        keyword Set Application Focus.

        See also `Assert Pattern Is Not Visible In Active App`, `Assert Pattern Is Not Visible In Region`, 
        and `Assert Pattern Is Visible In Region`.

        Example:
        | Set Application Focus                   | Calculator       |
        | Assert Pattern Is Visible in Active App | equalsbutton.png |
        # Asserts that pattern is visible in the new search region in active app as defined by offset values.
        """
        self._info("Asserting that pattern, '%s' is not visible in app." % (pattern))
        self.set_search_region_to_active_app()
        try:
            assert not exists(self._pattern_finder._find_pattern(pattern))
        except AssertionError, err:
            raise AssertionError("Pattern: %s is visible in search region." % (pattern))

    def assert_pattern_is_not_visible_in_region(self, pattern):
        """Assert that ``pattern`` is not visible in search region.
        See `introduction` for details about locating elements.

        This keyword must be paired with any of the following keywords:
        `Set Search Region To Target Screen`, `Set New Search Region In Active App`, 
        `Set Search Region To Application`, `Set New Search Region In Target Screen` or 
        `Set New Search Region In Application`.

        See also `Assert Pattern Is Not Visible In Active App`, 
        `Assert Pattern Is Visible In Active App` and `Assert Pattern Is Visible In Region`.

        Example 1:
        | Set New Search Region In Active App     | 10, 60, -20, -270 |
        | Assert Pattern Is Not Visible in Region | pattern.png       |
        # Asserts that pattern is visible in the new search region in active app as defined by offset values.

        Example 2:
        | Set New Search Region In Active Screen  | 10, 60, -20, -270 |
        | Assert Pattern Is Not Visible in Region | pattern.png       |
        # Asserts that pattern is visible in the new search region in active screen as defined by offset values.

        """
        self._info("Asserting that pattern, '%s' is not visible in app." % (pattern))
        try:
            assert not exists(self._pattern_finder._find_pattern(pattern))
        except AssertionError, err:
            raise AssertionError("Pattern: %s is visible in search region." % (pattern))