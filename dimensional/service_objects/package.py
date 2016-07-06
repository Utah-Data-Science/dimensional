import os
import tarfile

class Compressor(object):

    root_directory = None
    filename = None
    target_directory = None
    target = None
    replace = True

    def __init__(self, root_directory, filename=None, target_directory=None, replace=True):

        self._assert_root_directory(root_directory)

        self.root_directory = root_directory
        self.filename = filename or "{}.tgz".format(os.path.basename(root_directory))
        self.target_directory = target_directory or self._directory_of(self.root_directory)
        self.replace = replace
        self.target = os.path.join(self.target_directory, self.filename)

        self._assert_writeable_target()

    def _directory_of(self, base_directory):
        return os.path.abspath(os.path.dirname( base_directory ))

    def _assert_root_directory(self, root_directory):
        if not os.path.isdir(root_directory):
            raise IOError('Root directory not found: {}'.format(root_directory))

    def _assert_writeable_target(self):
        if not self.replace and os.path.exists(self.target):
            raise IOError('Target file already exists: {}. Try running with replace=True'.format(self.target))

        destination_directory = self._directory_of(self.target)
        if not os.path.isdir(destination_directory):
            raise IOError('Unknown destination: {}.'.format(destination_directory))

    def compress(self):
        with tarfile.open(self.target, "w:gz") as tar:
            tar.add(self.root_directory)
