import unittest

from dropbox2drive import main

class TestFileCompare(unittest.TestCase):
    def test(self):
        # for testing purposes we can get one random file.
        filename = "test_main_methods.py"
        f1 = TestFileCompare.regular_file_to_class(filename)
        f2 = TestFileCompare.regular_file_to_class(filename)
        self.assertEquals(f1, f2)

    @staticmethod
    def regular_file_to_class(filename):
        pass  # TODO


class TestClassifyFiles(unittest.TestCase):
    def test(self):
        files_to_update = []
        files_to_erase = []

        total_files = files_to_erase.extend(files_to_update)
        classified = main.classify_files(total_files, files_to_update)
        self.assertItemsEqual(files_to_update, classified["to_update"])
        self.assertItemsEqual(files_to_erase, classified["to_erase"])
