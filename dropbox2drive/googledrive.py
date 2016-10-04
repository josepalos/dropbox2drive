def get_files():
    """Returns a list with the files contained in this cloud system."""
    pass


def erase_files(files):
    """Remove the files in the drive cloud."""
    pass


def update_files(files):
    """
    Update the files into google drive from dropbox.

    Given a list of files to upload, it checks if the file in the cloud needs
    to be updated, and then update it if needed.
    If the file doesn't exist in the cloud, it's created.
    """
    pass


def serialize(file):
    """Convert the File class data to drive format."""
    pass


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
