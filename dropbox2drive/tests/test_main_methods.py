import unittest
import datetime
import tempfile
import filecmp
import os
import random
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
            original_file_stream=open(filename, 'rb'),
            last_modified=datetime.date.today(),
            metadata={"some": "random metadata"},
        )


class TestFileContentIsTheSame(unittest.TestCase):
    def test(self):
        f = getRandomTempFile()

        f1 = TestFileCompare.regular_file_to_class(f.name)
        self.assertTrue(filecmp.cmp(f.name, f1.tmp_file.name))


class TestClassifyFiles(unittest.TestCase):
    def test(self):
        files_to_update = list([])
        files_to_erase = list([])
        for _ in range(random.randint(1, 10)):
            r = getRandomTempFile()
            f = TestFileCompare.regular_file_to_class(r.name)
            files_to_update.append(f)

        for _ in range(random.randint(1, 10)):
            r = getRandomTempFile()
            f = TestFileCompare.regular_file_to_class(r.name)
            files_to_erase.append(f)

        total_files = list(files_to_erase)
        total_files.extend(files_to_update)

        classified = main.classify_files(files_to_update, total_files)
        self.assertItemsEqual(files_to_update, classified["to_update"])
        self.assertItemsEqual(files_to_erase, classified["to_erase"])


def getRandomTempFile():
    f = tempfile.NamedTemporaryFile(mode="arb")
    for _ in range(random.randint(1, 100)):
        f.write(os.urandom(2))
    return f
