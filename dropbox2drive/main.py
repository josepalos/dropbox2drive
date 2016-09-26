import googledrive
import dropbox


def classify_files(new_file_index, last_file_index):
    """
    Sort the files of last_file_index between to_erase and to_update.

    All the files existing in new_file_index will be put into the map inside
    the key 'to_update'. The files in last_file_index that no longer appear in
    the new index will be put into the key 'to_erase'.

    Returns a dict containing two keys: to_erase and to_update, and both of the
    values are lists of files.
    """
    pass


def main():
    """Main method."""
    # add some config methods to googledrive.py and dropbox.py

    new_file_index = dropbox.get_files()
    last_file_index = googledrive.get_files()
    files_sorted = classify_files(new_file_index, last_file_index)
    googledrive.erase_files(files_sorted.to_erase)
    googledrive.update_files(files_sorted.to_update)

if __name__ == "__main__":
    main()
