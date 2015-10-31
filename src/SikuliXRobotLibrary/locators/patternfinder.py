from SikuliXRobotLibrary import utils
import robot
from robot.api import logger
from sikuli import *

class PatternFinder(object):
    def __init__(self):
        self.locator = None

    # Private

    def _parse_locator(self, locator):
        """Breaks down locator details to pattern and sensitivity"""
        if not ".png" in locator:
            pattern = locator
            sensitivity = None
        elif ".png" in locator:
            if not locator.endswith('.png'):
                locator_parts = locator.partition('=')
                if len(locator_parts[1]) > 0:
                    pattern = locator_parts[0].strip()
                    sensitivity = locator_parts[2].strip()
            else:
                pattern = locator
                sensitivity = 0.70
        return (pattern, sensitivity)

    def _find_pattern(self, locator):
        """Sets pattern details if string or pattern is provided based on the parsed locator value"""
        assert locator is not None and len(locator) > 0
        locator = locator.strip().lower()
        (pattern, sensitivity) = self._parse_locator(locator)

        if (sensitivity != None):
            sensitivity = float(sensitivity)
            pattern = Pattern(pattern).similar(sensitivity)
        else:
            pattern = pattern
        return pattern

    def _parse_scroll_details(self, scroll):
        """Breaks down scroll details to scroll direction and scroll steps"""
        assert scroll is not None and len(scroll) > 0
        scroll = scroll.lower()
        scroll_parts = scroll.partition('=')
        if len(scroll_parts[1]) > 0:
            scroll_direction = scroll_parts[0].strip()
            scroll_steps = int(scroll_parts[2].strip())

        return (scroll_direction, scroll_steps)
