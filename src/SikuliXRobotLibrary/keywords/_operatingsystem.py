from sikuli import *
from keywordgroup import KeywordGroup

class _OperatingSystemKeywords(KeywordGroup):
    def __init__(self):
        self.env_OS = Env.getOS()
        self.env_OS_version = Env.getOSVersion()

    # Public

    def get_env_OS(self):
        """Returns the Operating System ``type`` of test pc.
        Example of Operating System `types`: WINDOWS, MAC, LINUX
        """
        self._info("OS version is '%s'." % self.env_OS)
        return self.env_OS

    def get_env_OS_version(self):
        """Returns the Operating System ``version`` of test pc.
        """
        self._info("OS is '%s'." % self.env_OS_version)
        return self.env_OS_version

    def get_env_OS_type_and_version(self):
        """Returns the Operating System ``type`` and ``version`` of test pc.
        """
        return str(self.env_OS) + " " + str(self.env_OS_version)

    # Check if OS version is correct based on the argument env_OS
    def confirm_env_OS(self, env_OS):
        """Returns `True` or `False` based on the `env_OS` version where the script is executed.
        """
        assert env_OS is not None and len(env_OS) > 0
        env_OS = env_OS.upper()
        if(env_OS == "WINDOWS"):
            OS_confirm = Settings.isWindows()
        elif (env_OS == "MAC"):
            OS_confirm = Settings.isMac()
        elif (env_OS == "LINUX"):
            OS_confirm = Settings.isLinux()
        self._info("OS confirmation: '%s'." % OS_confirm)
        return OS_confirm
