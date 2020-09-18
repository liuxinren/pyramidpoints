import os, glob




class FileUtils:

    def directory_check(self, directory):
        if directory.endswith('/'):
            return directory
        else:
            return directory + '/'

    def get_files_with_ext(self, directory, ext):
        return glob.glob(self.directory_check(directory) + '*%s' % ext)

    def get_file_basename(self, filename):
        return os.path.splitext(filename)

    def delete_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print("%s does not exist" % filename)

    def get_filename_only(self, filename):
        return os.path.basename(filename)

    def get_directory(self, filename):
        return os.path.dirname(filename)

    def get_file_without_ext(self, filename):
        return os.path.splitext(filename)[0]

    def get_file_prefix(self, filename):
        return self.get_file_basename(self.get_filename_only(filename))[0]


    def get_directory_file_prefixes(self, directory, ext=''):
        prefix_list = []
        files = self.get_files_with_ext(directory, ext)
        for f in files:
            prefix_list.append(self.get_file_prefix(f))

        return prefix_list
