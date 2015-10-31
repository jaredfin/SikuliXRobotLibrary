
from sikuli import *
from keywordgroup import KeywordGroup

class _ImageLibraryKeywords(KeywordGroup):
    def __init__(self):
        self.image_library_directory = None
        
    # Public
    
    def set_image_library(self, path):
        """ Set the default image library ``path`` where all image references will be accessed.
        This must be used during setup in order to set the image library before the test cases are executed.
        """
        self._info("Setting image library at '%s'." % path)
        self._set_image_library_directory(path)
        addImagePath(self.image_library_directory)

    # Private
    """***************************** Internal methods ************************************"""
    def _set_image_library_directory(self, path):
        if not self._path_exists(path):
            raise AssertionError("Path '%s' does not exist." % (path))
        else:
            self.image_library_directory = path

    def _get_image_library_directory(self):
        # Use the image library directory if set
        if self.image_library_directory is not None:
            return self.image_library_directory

