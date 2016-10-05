"""Google drive services."""
import os
import httplib2

import oauth2client
from apiclient import discovery
from oauth2client import client
from oauth2client import tools

# If modifying these scopes, delete your previously saved
# credentials at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'dropbox2drive-client_secret.json'
APPLICATION_NAME = 'dropbox2drive'
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


class GoogleDrive(object):
    """Represents the Drive Cloud service."""

    def __init__(self, parent_directory):
        self.parent_directory = parent_directory
        self.service = self._get_service()
        self.folders = {
            '/': self._get_id_folder(parent_directory)
        }

    def _get_credentials(self):
        """Get valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
        (~~From Google Drive API examples~~)

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'dropbox2drive.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def _get_service(self):
        credentials = self._get_credentials()
        http = credentials.authorize(httplib2.Http())
        return discovery.build('drive', 'v3', http=http)

    def get_files(self):
        """Return a list with the files contained in this cloud system."""
        # if it's a folder (MIME type 'application/vnd.google-apps.folder')
        # store to self.folders with the relative path as key, id as value
        pass

    def erase_files(self, files):
        """Remove the files in the drive cloud."""
        pass

    def update_files(self, files):
        """
        Update the files into google drive from dropbox.

        Given a list of files to upload, it checks if the file in the cloud
        needs to be updated, and then update it if needed.
        If the file doesn't exist in the cloud, it's created.
        """
        pass

    def _get_id_folder(self, path, parent_id=None):
        """
        Return the drive id of the specified folder.

        If the folder doesn't exist, it is created.
        """
        current_folder, path_tail = os.path.split(path)
        if current_folder == "":
            current_folder = path_tail
            path_tail = ""
        page_token = None
        q = "mimeType = 'application/vnd.google-apps.folder'"
        if parent_id is not None:
            q = q + (" and '%s' in parents" % parent_id)

        while True:
            response = self.service.files() \
                .list(
                      orderBy='name',
                      q=q,
                      spaces='drive',
                      fields='nextPageToken, files(id, name)',
                      pageToken=page_token
                      ).execute()
            for file in response.get('files', []):
                # Process change
                if file.get('name') == current_folder:
                    if path_tail == "":
                        return file.get('id')
                    else:
                        return self._get_id_folder(path_tail, file.get('id'))
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

    def _create_folder(self, path):
        """Create a folder in the drive."""
        # From google api docs:
        # file_metadata = {
        #  'name' : 'Invoices',
        #  'mimeType' : 'application/vnd.google-apps.folder'
        # }
        # f = drive_service.files().create(body=file_metadata, fields='id').execute()
        pass

    def _parse_metadata(self, f):
        """Map the metadata of the File object to drive request format."""
        pass

    def serialize(self, f):
        """Convert the File class data to drive format."""
        return {
            'body': {
                'name': f.name,
                'parents': [self._get_id_folder(f.relative_path)],
            },
            'media_body': f.tmp_file
        }.update(self._parseMetadata(f))


"""
    https://developers.google.com/drive/v2/reference/files
    ______________FILE FORMAT__________________________
    kind (string): the type of the file (Always "drive#file")
    id (string): id of the file (w)
    etag (etag): etag of the file
    selfLink (string): link back to this file
    title (string): title of the file. Used to identify file or folder name (w)
    mimeType (string): only mutable on update new content. can be blank (w)
    description (string): a hort description of the file (w)
    labels (object): (w)
    {
        .starred (boolean): the file is starred by the user (w)
        .hidden (boolean): --DEPRECATED (w)
        .trashed (boolean): the file has been trashed (w)
        .restricted (boolean): viewers are prevented from downl, print, copy. (w)
        .viewed (boolean): the file has been seen by the user. (w)
    }
    createdDate (datetime): formatted RFC 3339 timestamp
    modifiedDate (datetime): only mutable when the param setModifiedDate=true(w)
    modifiedByMeDate (datetime): last time this user modified.
    downloadUrl (string)
    indexableText (object): (only writable)
    {
        .text (string): text to be indexed
    }
    userPermission (nested object): permissions for the authenticated user on
        this file
    fileExtension (string): final component of fullFileExtension.
    md5Checksum (string)
    fileSize (long)
    alternateLink (string): for opening the file in a relevant google editor or
        viewer
    embedLink (string)
    sharedWithMeDate (datetime)
    parents[] (list): (w)
    exportLinks (map):
    {
        .(key) (string): mapping from export format to url.
    }
    originalFilename (string): -or else the original value of the title field. (w)
    quotaBytesUsed (long)
    ownerNames[] (list)
    lastModifyingUserName (string)
    editable (boolean): by the current user
    writersCanShare (boolean): (w)
    thumbnailLink (string)
    lastViewedByMeDate (datetime)
    webContentLink (string)
    explicitlyTrashed (boolean)
    imageMediaMetadata (object): only for imagetypes, content depend on what can be
        parsed
    {
        .width (int)
        .height (int)
        .rotation (int): clockwise degrees
        .location (object)
            .latitude (double)
            .longitude (double)
            .altitude (double)
            .date (string): EXIF format timestamp
            .cameraModel (string)
            .exposureTime (float)
            .aperture (float)
            .flashUsed (boolean)
            .focalLength (float)
            .isoSpeed (integer)
            .meteringMode (string)
            .sensor (string)
            .exposureMode (string)
            .colorSpace (string)
            .whiteBalance (string)
            .exposureBias (float)
            .maxApertureValue (float)
            .subjectDistance (int)
            .lens (string)
    }
    thumbnail (object)
    {
        .image (bytes): URL-safe Base64 encoded bytes. (conform to RFC 4648 sect 5)
        .mimeType (string)
    }
    webViewLink (string):  	A link only available on public folders for viewing
        their static web assets (HTML, CSS, JS, etc) via Google Drive's Website
        Hosting.
    iconLink (string)
    shared (boolean)
    owners[] (list of users)
    lastModifyingUser (user)
    appDataContents (boolean): in the Application Data folder.
    openWithLinks (map): map for each of the user's apps to a link to open this
        file with an app. Only populated when the drive.apps.readonly scope is used
    {
        .(key): (string)
    }
    defaultOpenWithLink (string): link to open this file with the default app.
        Only populated when the drive.apps.readonly scope is used
    headRevisionId (string): ID of the file's head revision. Only populated for
        files with content stored in Drive, not G.Docs or shortcut files.
    copyable (boolean)
    properties[] (list): (w)
    markedViewedByMeDate (datetime): --DEPRECATED-- (w)
    version (long
    sharingUser (user)
    permissions[] (list)
    videoMediaMetadata (object)
    {
        .width (int)
        .height (int)
        .durationMillis (long)
    }
    folderColorRgb (string): (w)
    fullFileExtension (string)
    ownedByMe (boolean)
    canComment (boolean)
    shareable (boolean)
    spaces[] (list): list of spaces which contain the file. Supported are: 'drive',
        'appDataFolder' and 'photos'.
    canReadRevisions (boolean)
    isAppAuthorized (boolean)

    __________________USER FORMAT__________________________
    .kind (string): Always "drive#user"
    .displayName (string)
    .picture (object):
    {
        .url (string)
    }
    .isAuthenticatedUser (boolean): the user is who made the request.
    .emailAddress (string)
    .permissionId (string)
"""
