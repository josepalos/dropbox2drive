import unittest
import datetime
import tempfile
from dropbox2drive import main


class TestFileCompare(unittest.TestCase):
    def test(self):
        # for testing purposes we use a temporari nonsense file.
        f = tempfile.NamedTemporaryFile()
        f.write("Some random data inside the file\x00\x09\x48\x94\x48....")
        f_different = tempfile.NamedTemporaryFile()
        f_different.write("diferent data")

        f1 = TestFileCompare.regular_file_to_class(f.name)
        f2 = TestFileCompare.regular_file_to_class(f.name)
        f3 = TestFileCompare.regular_file_to_class(f_different.name)
        self.assertEquals(f1, f2)
        self.assertNotEquals(f1, f3)

        f.close()
        f_different.close()

    @staticmethod
    def regular_file_to_class(filename):
        return main.File(
            name=filename,
            relative_path=filename,
            cloud={'name': 'test', 'tmp_dir': 'test'},
            original_file=filename,
            last_modified=datetime.date.today(),
            metadata={"some": "random metadata"},
        )


class TestClassifyFiles(unittest.TestCase):
    def test(self):
        files_to_update = []
        files_to_erase = []

        total_files = files_to_erase.extend(files_to_update)
        classified = main.classify_files(total_files, files_to_update)
        self.assertItemsEqual(files_to_update, classified["to_update"])
        self.assertItemsEqual(files_to_erase, classified["to_erase"])
