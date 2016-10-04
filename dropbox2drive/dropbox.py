def get_files():
    """Returns a list with the files contained in this cloud system."""
    pass


def deserialize(file):
    """Convert the dropbox file format to File class."""
    pass

"""
name (String): The last component of the path (including extension). This never
    contains a slash.
id (String): min_length=1
client_modified (Timestamp): (%Y-%m-%dT%H:%M:%SZ) For files, this is the
    modification time set by the desktop client when the file was added to
    Dropbox. Since this time is not verified (the Dropbox server stores
    whatever the desktop client sends up), this should only be used for display
    purposes (such as sorting) and not, for example, to determine if a file has
    changed or not.
server_modified (Timestamp)
rev (String): (min_length=9, pattern="[0-9a-f]+") A unique identifier for the
    current revision of a file. This field is the same rev as elsewhere in the
    API and can be used to detect changes and avoid conflicts.
size (UInt64): The file size in bytes.
path_lower (String)?: The lowercased full path in the user's Dropbox. This
    always starts with a slash. This field will be null if the file or folder
    is not mounted.
path_display (String)?: The cased path to be used for display purposes only.
parent_shared_folder_id (String)?: (pattern="[-_0-9a-zA-Z:]+") --Deprecated--
    Please use FileSharingInfo.parent_shared_folder_id or
    FolderSharingInfo.parent_shared_folder_id instead.
media_info (MediaInfo)?: Additional information if the file is a photo or
    video.
{
MediaInfo (union)
    .pending (Void): Indicate the photo/video is still under processing and
        metadata is not available yet.
    .metadata (MediaMetadata): The metadata for the photo/video.
    {
    MediaMetadata (datatype with subtypes)
        --photo (PhotoMetadata)
        {
            .dimensions (Dimensions)?
            {
                .height (UInt64)
                .width (UInt64)
            }
            .location (GpsCoordinates)?
            {
                .latitude (Float64)
                .longitude (Float64)
            }
            .time_taken ("%Y-%m-%dT%H:%M:%SZ")?
        }
        --video (VideoMetadata)
        {
            .dimensions (Dimensions)?
            .location (GpsCoordinates)?
            .duration (UInt64): in milliseconds
        }
    }
}
sharing_info (FileSharingInfo)? Set if this file is contained in a shared
    folder.
{
    .read_only (Boolean) True if the file or folder is inside a read-only
        shared folder.
    .parent_shared_folder_id (String): (pattern="[-_0-9a-zA-Z:]+") ID of shared
        folder that holds this file.
    .modified_by (String)?: (min_length=40, max_length=40) The last user who
        modified the file. This field will be null if the user's account has
        been deleted.
}
property_groups (List of PropertyGroup)? Additional information if the file has
    custom properties with the property template specified.
{
    Collection of custom properties in filled property templates. This datatype
    comes from an imported namespace originally defined in the properties
    namespace.
    .template_id (String): (min_length=1, pattern="(/|ptid:).*") A unique
        identifier for a property template type.
    .fields (List of PropertyField): up to 32 for a template
    {
        .name (String): up to 256B
        .value (String): up to 1024B
    }
}
has_explicit_shared_members (Boolean)?: This flag will only be present if
    include_has_explicit_shared_members is true in list_folder or get_metadata.
    If this flag is present, it will be true if this file has any explicit
    shared members. This is different from sharing_info in that this could be
    true in the case where a file has explicit members but is not contained
    within a shared folder.
"""
