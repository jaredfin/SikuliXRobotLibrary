
import time
import robot
from sikuli import *
from keywordgroup import KeywordGroup
from SikuliXRobotLibrary.locators import PatternFinder
from SikuliXRobotLibrary import utils

class _WaitingKeywords(KeywordGroup):
    def __init__(self):
        self._pattern_finder = PatternFinder()
        self.sikulix_timeout = None
        self.sikulix_scanrate = None

    # Public

    def set_sikulix_timeout(self, timeout):
        """Sets the ``sikulix timeout`` value.

        See `introduction` for details about `sikulix_timeout`.
        """
        if self.sikulix_timeout is not None:
            self.sikulix_timeout = float(self._clean_string(timeout))

        self._info("Setting sikulix timeout to '%s' seconds." % (self.sikulix_timeout))
        Settings.AutoWaitTimeout(self.sikulix_timeout)

    def set_sikulix_scanrate(self, scanrate):
        """Sets the ``sikulix scanrate`` value.

        See `introduction` for details about `sikulix_scanrate`.
        """
        if self.sikulix_scanrate is not None:
            self.sikulix_scanrate = float(self._clean_string(scanrate))

        self._info("Setting sikulix scanrate to '%s' seconds." % (self.sikulix_scanrate))
        Settings.AutoWaitTimeout(self.sikulix_scanrate)

    def wait_in_seconds(self, timeout):
        """Waits until ``timeout`` expires.

        See also `Wait For Pattern To Be Visible`, `Wait Until Pattern Is Visible`, 
        `Wait For Pattern To Vanish` and `Wait Until Pattern Vanish`.
        """
        timeout = float(self._clean_string(timeout))
        self._info("Setting wait value to '%s' seconds." % (timeout))
        wait(timeout)

    def wait_for_pattern_to_be_visible(self, pattern):
        """Waits until ``pattern`` appears on `application` in focus. 
        Fails if ``pattern`` is not immediately visible on `application` in focus.
        SikuliX's default timeout is 3 seconds.

        See also `Wait In Seconds`, `Wait Until Pattern Is Visible`, 
        `Wait For Pattern To Vanish` and `Wait Until Pattern Vanish`.
        """
        self.set_search_region_to_active_app()
        self._info("Waiting for pattern '%s' to be visible." % (pattern))
        try:
            pattern = self._pattern_finder._find_pattern(pattern)
            wait(pattern)
        except FindFailed, err:
            raise AssertionError("Element locator '%s' did not match any elements" % (pattern))

    def wait_until_pattern_is_visible(self, pattern, timeout):
        """Waits until ``pattern`` appears on `application` in focus at specified ``timeout``.
        
        ``timeout`` value may be set to a `float` or to ``FOREVER``.

        Using ``FOREVER`` as timeout will execute the script
        to infinity unless the pattern appears

        Otherwise, Fails if ``timeout`` expires before the ``pattern`` appears.

        See also `Wait In Seconds`, `Wait For Pattern To Be Visible`, 
        `Wait For Pattern To Vanish` and `Wait Until Pattern Vanish`.
        """
        self._info("Setting wait value to '%s'." % (timeout))
        self.set_search_region_to_active_app()
        try:
            timeout = self._clean_string(timeout)
            pattern = self._pattern_finder._find_pattern(pattern)
            if (timeout == "FOREVER"):
                wait(pattern, FOREVER)
            else:
                timeout = float(timeout)
                wait(pattern, timeout)
        except FindFailed, err:
            raise AssertionError("Element locator '%s' did not match any elements after %s" % (pattern, timeout))

    def wait_for_pattern_to_vanish(self, pattern):
        """Waits until ``pattern`` disappears on `application` in focus.
        Fails if ``pattern`` is not immediately hidden on `application` in focus.
        SikuliX's default timeout is 3 seconds.

        See also `Wait In Seconds`, `Wait For Pattern To Be Visible`,
        `Wait Until Pattern Is Visible`, and `Wait Until Pattern Vanish`.
        """
        self._info("Waiting for pattern '%s' to vanish." % (pattern))
        self.set_search_region_to_active_app()
        pattern = self._pattern_finder._find_pattern(pattern)
        hidden = waitVanish(pattern)
        self._debug(hidden)

        if not hidden:
           raise AssertionError("Element '%s' was still visible" % (pattern))

    def wait_until_pattern_vanish(self, pattern, timeout):

        """Waits until ``pattern`` disappears on `application` in focus at specified ``timeout``.
        
        ``timeout`` value may be set to a `float` or to ``FOREVER``.

        Using ``FOREVER`` as timeout will execute the script
        to infinity unless the pattern appears

        Otherwise, Fails if ``timeout`` expires before the ``pattern`` appears.

        See also `Wait In Seconds`, `Wait For Pattern To Be Visible`
        `Wait For Pattern To Be Visible`, `Wait For Pattern To Vanish`.
        """
        self._info("Setting wait value to '%s'." % (timeout))
        self.set_search_region_to_active_app()
        timeout = self._clean_string(timeout)
        pattern = self._pattern_finder._find_pattern(pattern)
        hidden = None
        if (timeout == "FOREVER"):
            hidden = waitVanish(pattern, FOREVER)
        else:
            timeout = float(timeout)
            hidden = waitVanish(pattern, timeout)
        self._debug(hidden)
        
        if not hidden:
           raise AssertionError("Element '%s' was still visible in %s" % (pattern, timeout))

    # Private
    """***************************** Internal methods ************************************"""
    def _clean_string(self, string_param):
        assert string_param is not None and len(string_param) > 0
        string_param = string_param.strip()
        return string_param

    def _get_sikulix_timeout(self):
        # Use sikulix_timeout value if set
        if self.sikulix_timeout is not None:
            return self.sikulix_timeout

        # Otherwise use SikuliX's default timeout
        return getAutoWaitTimeout()

    def _get_sikulix_scanrate(self):
        # Use sikulix_timeout value if set
        if self.sikulix_scanrate is not None:
            return self.sikulix_scanrate

        # Otherwise use SikuliX's default scanrate
        return getWaitScanRate()