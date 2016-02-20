from sikuli import *
from keywordgroup import KeywordGroup
from SikuliXRobotLibrary.locators import PatternFinder
from SikuliXRobotLibrary import utils

class _RegionKeywords(KeywordGroup):
    def __init__(self):
        # Set target coordinates to Screen 1 as default
        self.target_screen = None
        self._pattern_finder = PatternFinder()

    # Public

    def set_search_region_to_target_screen(self, target_screen):
        """Sets the ROI or the search area to a specified ``target_screen``.
        Searching for pattern match is faster if the search region is smaller.

        For more information on multi-monitor environment, see https://sikulix-2014.readthedocs.org/en/latest/screen.html

        See also `Set Search Region To Active App`, `Set New Search Region In Active App`, `Set Search Region To Application`
        `Set New Search Region In Target Screen`, and `Set New Search Region In Application`.

        Example:
        | Set Search Region To Target Screen | Screen 0 | # Sets ROI to the Primary Monitor  |
        | Set Search Region To Target Screen | Screen 1 | # Sets ROI to Additional Monitor 1 |
        | Set Search Region To Target Screen | Screen 2 | # Sets ROI to Additional Monitor 2 |
        | Set Search Region To Target Screen | Screen 3 | # Sets ROI to Additional Monitor 3 |

        """
        self._info("Setting search region to '%s'." % target_screen)
        self.target_screen = target_screen
        screen_number = self._parse_target_screen(self.target_screen)
        setROI(Region(Screen(screen_number)))
        #setRect(Region(Screen(screen_number)))

    def set_search_region_to_active_app(self):
        """Sets the ROI or the search area to the application in focus.
        Searching for pattern match is faster if the search region is smaller.

        Example:
        | Set Search Region To Active App | # Sets the search region to the application in focus | 

        See also `Set Search Region To Target Screen`, `Set New Search Region In Active App`, `Set Search Region To Application`,
        `Set New Search Region In Target Screen` and `Set New Search Region In Application`.
        """
        self._info("Setting the search region to the active application.")
        search_region = self.get_active_app_region()
        self._info("Setting the search region to '%s'." % (search_region))
        setROI(search_region)
        #setRect(search_region)

    def set_search_region_to_application(self, app_name):
        """Sets the ROI or the search area to the application as specified in `app_name`.
        Searching for pattern match is faster if the search region is smaller.

        Example:
        | Set Search Region To Application | Calculator | # Sets the search region to the Calculator application. | 

        See also `Set Search Region To Target Screen`, `Set New Search Region In Active App`,
        `Set New Search Region In Target Screen` and `Set New Search Region In Application`.
        """
        search_region = App(app_name).window()
        self._info("Setting the search region: '%s' to the application: '%s'." % (app_name, search_region))
        setROI(search_region)
        #setRect(search_region)

    def set_new_search_region_in_active_app(self, offsets):
        """Sets new ROI or the search area to a specified ``offsets`` based on original coordinate values of active application in focus.

        See also `Set Search Region To Target Screen`, `Set Search Region To Active App`, `Set Search Region To Application`,
        `Set New Search Region In Target Screen`.

        Example:
        | Set New Search Region In Active App | 10, 60, -20, -270 | 
        # Offsets x, y, height, width to 10, 60, -20, -270 pixels respectively.
        """
        self._info("Setting new search region to offsets '%s'." % offsets)
        (offsetx, offsety, offsetw, offseth) = self._parse_coordinate_offsets(offsets)
        active_app_region = self.get_active_app_region()
        self._info("Active app region '%s'." % active_app_region)
        new_x = active_app_region.x + offsetx
        new_y = active_app_region.y + offsety
        new_w = active_app_region.w + offsetw
        new_h = active_app_region.h + offseth
        new_coordinates = (new_x, new_y, new_w, new_h)
        
        self._info("New coordinates: x:'%s' y:'%s w:'%s h:'%s." % new_coordinates)
        setROI(*new_coordinates)
        #setRect(*new_coordinates)

    def set_new_search_region_in_application(self, app_name, offsets):
        """Sets new ROI or the search area to a specified ``offsets`` based on original coordinate values of application as specified in `app_name`.

        See also `Set Search Region To Target Screen`, `Set Search Region To Active App`, `Set Search Region To Application`,
        and `Set New Search Region In Target Screen`.

        Example:
        | Set New Search Region In Application | Calculator | 10, 60, -20, -270 | 
        # Offsets x, y, height, width to 10, 60, -20, -270 pixels respectively.
        """
        self._info("Setting new search region to offsets '%s'." % offsets)
        (offsetx, offsety, offsetw, offseth) = self._parse_coordinate_offsets(offsets)
        application_region = self.get_application_region(app_name)
        self._info("Application region '%s'." % application_region)
        new_x = application_region.x + offsetx
        new_y = application_region.y + offsety
        new_w = application_region.w + offsetw
        new_h = application_region.h + offseth
        new_coordinates = (new_x, new_y, new_w, new_h)
        
        self._info("New coordinates: x:'%s' y:'%s w:'%s h:'%s." % new_coordinates)

        setROI(*new_coordinates)
        #setRect(*new_coordinates)

    def set_new_search_region_in_target_screen(self, target_screen, offsets):
        """Sets new ROI or new search area to a specified ``offsets`` based on original coordinate values of `target screen`.

        See also `Set Search Region To Target Screen`, `Set New Search Region In Active App`, `Set Search Region To Application`,
        `Set Search Region To Active App` and `Set New Search Region In Application`.

        Example:
        | Set New Search Region In Target Screen | Screen 0 | 10, 60, -20, -270 |
        # Offsets x, y, height, width of the Primary Monitor to 10, 60, -20, -270 pixels respectively.
        """
        self._info("Setting new search region to offsets '%s' of '%s'." % (offsets, target_screen))
        self.target_screen = target_screen
        (offsetx, offsety, offsetw, offseth) = self._parse_coordinate_offsets(offsets)
        screen_number = self._parse_target_screen(self.target_screen)
        self._info("'%s' region '%s'." % (target_screen, screen_number))

        new_x = Sceen(screen_number).x + offsetx
        new_y = Sceen(screen_number).y + offsety
        new_w = Sceen(screen_number).w + offsetw
        new_h = Sceen(screen_number).h + offseth
        new_coordinates = (new_x, new_y, new_w, new_h)
        
        self._info("New coordinates: x:'%s' y:'%s w:'%s h:'%s." % new_coordinates)
        setROI(*new_coordinates)
        #setRect(*new_coordinates)

    def get_screen_coordinates(self, target_screen):
        """Returns the ``coordinates`` of the screen as specified in `target_screen`.

        Example:
        | Get Screen Coordinates | 0 | # Gets the coordinates of Screen 0 |
        | Get Screen Coordinates | 1 | # Gets the coordinates of Screen 1 |
        """
        screen_number = self._parse_target_screen(target_screen)
        coordinates = (Screen(screen_number).getX(), 
                       Screen(screen_number).getY(), 
                       Screen(screen_number).getW(), 
                       Screen(screen_number).getH())
        return coordinates

    def get_active_app_coordinates(self):
        """Returns the ``coordinates`` of the `application` in focus.
        Keyword must be combined with `Set Application Focus`.

        Examples:
        | Set Application Focus      | My Awesome App | # Sets the focus to `My Awesome App`       |
        | Get Active App Coordinates |                | # Gets the coordinates of `My Awesome App` |
        """
        activeWindow = App.focusedWindow()
        coordinates = (activeWindow.getX(), 
                       activeWindow.getY(), 
                       activeWindow.getW(), 
                       activeWindow.getH())
        return coordinates

    def get_application_coordinates(self, app_name):
        """Returns the ``coordinates`` of the `application` in focus.

        Example:
        | Get Application Coordinates | My Awesome App | # Gets the coordinates of `My Awesome App` |
        """
        applicationWindow = App(app_name).window()
        coordinates = (applicationWindow.getX(), 
                       applicationWindow.getY(), 
                       applicationWindow.getW(), 
                       applicationWindow.getH())
        return coordinates

    def get_application_xywh_coordinate(self, app_name, coordinate_name):
        """Returns the ``x``, ``y`` coordinate or the ``width`` or ``height`` of the `application` as specified in `app_name`.

        Examples:
        | Get Application XYWH Coordinates | My App | x | # Gets the x coordinate of `My App` |
        | Get Application XYWH Coordinates | My App | y | # Gets the y coordinate of `My App` |
        | Get Application XYWH Coordinates | My App | w | # Gets the w coordinate of `My App` |
        | Get Application XYWH Coordinates | My App | h | # Gets the h coordinate of `My App` |
        """
        self._info("Getting'%s' value for application '%s." % (coordinate_name, app_name))
        assert coordinate_name is not None and len(coordinate_name) > 0
        applicationWindow = App(app_name).window()
        if (coordinate_name == x):
            return applicationWindow.x
        elif (coordinate_name == y):
            return applicationWindow.y
        elif (coordinate_name == w):
            return applicationWindow.w
        elif (coordinate_name == h):
            return applicationWindow.h
        else:
            raise ValueError("Invalid value for coordinate name, input value is: '%s'" % (coordinate_name))

    def get_active_app_xywh_coordinate(self, coordinate_name):
        """Returns the ``x``, ``y`` coordinate or the ``width`` or ``height`` of the active application in focus.

        Examples:
        | Get Active App XYWH Coordinates | x | # Gets the x coordinate of the active application or the application in focus |
        | Get Active App XYWH Coordinates | y | # Gets the y coordinate of the active application or the application in focus |
        | Get Active App XYWH Coordinates | w | # Gets the w coordinate of the active application or the application in focus |
        | Get Active App XYWH Coordinates | h | # Gets the h coordinate of the active application or the application in focus |
        """
        self._info("Getting'%s' value for application '%s." % (coordinate_name, app_name))
        assert coordinate_name is not None and len(coordinate_name) > 0
        activeWindow = App.focusedWindow()
        if (coordinate_name == x):
            return activeWindow.x
        elif (coordinate_name == y):
            return activeWindow.y
        elif (coordinate_name == w):
            return activeWindow.w
        elif (coordinate_name == h):
            return activeWindow.h
        else:
            raise ValueError("Invalid value for coordinate name, input value is: '%s'" % (coordinate_name))

    def get_reference_pattern_coordinates(self, pattern):
        """Returns the ``coordinates`` of the element identified by ``pattern``.

        Example:
        | Get Reference Pattern Coordinates | pattern.png = 0.90 | # Gets the coordinates of pattern.png |
        """
        try:
            matched_pattern = find(self._pattern_finder._find_pattern(pattern))
            coordinates = (matched_pattern.getX(), matched_pattern.getY(), matched_pattern.getW(), matched_pattern.getH())
            return coordinates
        except FindFailed, err:
            raise AssertionError("Unable to find matching pattern '%s'." % (pattern))

    def get_application_region(self, app_name):
        """Returns the ``region`` of the application as specified in `app_name`.
        """
        return Region(*self.get_application_coordinates(app_name))


    def get_active_screen_region(self):
        """Returns the ``region`` of the active screen.
        """
        return Region(*self.get_active_screen_coordinates())

    def get_active_app_region(self):
        """Returns the ``region`` of the `application` in focus.
        """
        return Region(*self.get_active_app_coordinates())

    def get_reference_pattern_region(self, pattern):
        """Returns the ``region`` of the element identified by `pattern`.
        """
        return Region(*self.get_reference_pattern_coordinates(pattern))

    def get_last_matching_coordinates(self):
        """Returns the ``coordinates`` of the last region of interest or ROI.
        """
        coordinates_last_match = (getX(), getY(), getW(), getH())
        return coordinates_last_match

    def get_last_matching_region(self):
        """Returns the ``region`` of the last region of interest or ROI.
        """
        return Region(*self.get_last_matching_coordinates())

    # Private
    """***************************** Internal Methods ************************************"""

    def _parse_coordinate_offsets(self, offsets):
        assert offsets is not None and len(offsets) > 0
        offsets = offsets.split(',')
        offset_list = []
        for offset in offsets:
            offset_list.append(int(self._clean_string(offset)))
        return offset_list

    def _parse_target_screen(self, target_screen):
        assert target_screen is not None and len(target_screen) > 0
        target_screen = target_screen.lower().replace("screen", "").strip()
        target_screen = int(target_screen)

        actual_screen_count = getNumberScreens()
        if (actual_screen_count < target_screen):
            raise ValueError("Actual screen count: '%s' is less than the specified target screen." % (actual_screen_count, target_screen))
        return target_screen

    def _get_target_screen(self):
        if self.target_screen is not None:
            return self.target_screen
