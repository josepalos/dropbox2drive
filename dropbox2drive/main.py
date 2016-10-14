import googledrive
import dropbox
import filecmp
import tempfile
import os


class File(object):
    """Representation of a file."""  # TODO

    def __init__(self,
                 name,
                 relative_path,
                 cloud,
                 original_file_stream,
                 last_modified,
                 metadata=None,  # TODO, some common metadata structure
                 ):
        self.name = name
        self.relative_path = relative_path
        self.cloud = cloud
        self.last_modified = last_modified
        self.metadata = metadata
        # if the dir doesn't exist for this cloud, create it
        cloud_dir = os.path.join(tempfile.gettempdir(), cloud['tmp_dir'])
        if not os.path.exists(cloud_dir):
            os.makedirs(cloud_dir)
        self.tmp_file = tempfile.NamedTemporaryFile(dir=cloud_dir)
        self.tmp_file.write(original_file_stream.read())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                     self.name == other.name and
                     self.relative_path == other.relative_path and
                     self.last_modified == other.last_modified and
                     self.metadata.__eq__(other.metadata) and
                     filecmp.cmp(self.tmp_file.name, other.tmp_file.name)
                    )
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "{}: {} {}".format(
            self.__class__.__name__,
            self.name,
            self.tmp_file
        )


def classify_files(new_file_index, last_file_index):
    """
    Sort the files of last_file_index between to_erase and to_update.

    All the files existing in new_file_index will be put into the map inside
    the key 'to_update'. The files in last_file_index that no longer appear in
    the new index will be put into the key 'to_erase'.

    Returns a dict containing two keys: to_erase and to_update, and both of the
    values are lists of files.
    """
    files = {'to_erase': [], 'to_update': []}
    for f in last_file_index:
        if f in new_file_index:
            files["to_update"].append(f)
        else:
            files["to_erase"].append(f)
    return files


def main():
    """Main method."""
    # add some config methods to googledrive.py and dropbox.py
    gd = googledrive.GoogleDrive("testing_dropbox2drive")
    new_file_index = dropbox.get_files()
    last_file_index = gd.get_files()
    files_sorted = classify_files(new_file_index, last_file_index)
    gd.erase_files(files_sorted["to_erase"])
    gd.update_files(files_sorted["to_update"])

if __name__ == "__main__":
    main()
