from sikuli import *
import os
from keywordgroup import KeywordGroup

class _ApplicationKeywords(KeywordGroup):
    def __init__(self):
        self.application_name = None
        self.application_path = None
    
    # Public
    
    def set_application_focus(self, app_name):
        """Sets focus to the open ``application`` matching the given ``app_name``.
        
        Example:
        | Set Application Focus | My Awesome App | # Sets the focus to My Awesome App |
        """
        self._info("Setting focus at application '%s'." % app_name)
        self._set_application_name(app_name)
        try:
            App.focus(self.application_name)
        except FinFailed, err:
            raise AssertionError("Application '%s' not found." % (app_name))

    def switch_application_focus(self, app_name):
        """Switches focus to the open ``application`` matching the given ``app_name``.

        Example:
        | Set Application Focus    | My Awesome App      | # Switches  the focus to `My Awesome App` application  |
        | Switch Application Focus | My Very Awesome App | # Switches  the focus to `My Very Awesome App`         |
        """
        self._info("Switching focus to application '%s'." % app_name)
        self._set_application_name(app_name)
        try:
            switchApp(self.application_name)
        except FinFailed, err:
            raise AssertionError("Application '%s' not found." % (app_name))

    def check_and_open_application(self, app_name, path):
        """Checks if application is running and sets the focus to the application, 
        otherwise, opens application matching the given ``app_name`` and ``path``.

        Example:
        | Open Application | My Awesome App | C:/Program Files (x86)/Awesome App/awesomeapp.exe | # Opens `My Awesome App`, if app is already running, sets the focus to the app |

        See also `Close Application`, `Open Application`, 
        and `Application Is Running`
        """
        self._info("Opening application '%s' in path '%s'." % (app_name, path))
        if os.path.exists(path):
            self._set_application_path(path)
            self._set_application_name(app_name)

            if not App(self.application_name).isRunning():
                App.open(self.application_path)
            else:
                App.focus(app_name)
        else:
            raise AssertionError("Application path '%s' not found." % (path))

    def close_application(self, app_name):
        """Checks if the application matching the given ``app_name`` is running then closes it.

        See also `Check And Open Application`, `Open Application` and `Application Is Running`
        """
        self._info("Closing application '%s'." % app_name)
        self._set_application_name(app_name)
        if App(self.application_name).isRunning():
            App.close(self.application_name)

    def open_application(self, application_path):
        """opens the application matching the given ``application_path``.

        See also `Check And Open Application`, `Close Application` and `Application Is Running`
        """
        if os.path.exists(application_path):
            App.open(application_path)
        else:
            raise AssertionError("Application path '%s' not found." % (path))

    def application_is_running(self, app_name):
        """Returns `True` if application as specified in `app_name` is running, else, returns `False`.

        See also `Check And Open Application`, `Close Application`, and `Open Application`.
        """
        return App(app_name).isRunning()

    def run_command(self, command):
        """Runs a command, script or application path as specified in `command`.

        Example:
        | Run Command | control appwiz.cpl | # Opens the Windows Control Panel > Programs and Features window. |
        """
        run(script)

    def app_has_window(self, app_name):
        """Returns `True` if application's window or dialog as specified in `app_name` is open,
        else, returns `False`.

        See also `App Get Process ID`, `App Get Name` and `App Get Window`.
        Example:
        | App Has Window | Calculator | # Returns `True` if Calculator app is running in windows, else `False`. |
        """
        return App(app_name).hasWindow()

    def app_get_process_ID(self, app_name):
        """Returns the application's process ID as number if app is running, -1 otherwise.

        See also `App Has Window`, `App Get Name` and `App Get Window`.

        Example:
        | App Get Process ID | Calculator | # Returns a PID number if Calculator app is running in windows, else `-1`. |
        """
        return App(app_name).getPID()

    def app_get_name(self, app_name):
        """Returns the application's short name as show in the process list.

        See also `App Has Window`, `App Get Process ID` and `App Get Window`.

        Example:
        | App Get Name | Calculator | # Returns `calc.exe` if Calculator app is running in windows. |
        """
        return App(app_name).getName()


    def app_get_window(self, app_name):
        """Returns the title of the frontmost window of the application as specified in `app_name`, 
        might be an empty string

        See also `App Has Window`, `App Get Process ID` and `App Get Name`.

        Example:
        | App Get Window | Calculator | # Returns `Calculator` if Calculator app is running in windows. |
        """
        return App(app_name).getWindow()

    # Private
    """***************************** Internal Methods ************************************"""
    def _set_application_name(self, application_name):
        self.application_name = application_name

    def _get_application_name(self):
        if self.application_name is not None:
            return self.application_name

    def _set_application_path(self, application_path):
        if not self._path_exists(application_path):
            raise AssertionError("Path '%s' does not exist." % (application_path))
        else:
            self.application_path = application_path

    def _get_application_path(self):
        if self.application_path is not None:
            return self.application_path