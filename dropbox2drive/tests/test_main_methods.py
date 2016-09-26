import unittest

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
