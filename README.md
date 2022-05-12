# Rename-Musics-By-Metadata
Rename your music files (FLAC and WAV) with metadata.

<!-- Import image -->
![Example](/images/example1.jpg)

## How it works
Your music files are in a folder. This script will rename your files with the metadata.

The metadata is read from the file's tags. Hence you need the files to have the tags 'title' and 'tracknumber'.

## How to use
1. Open your terminal or command prompt (powershell is fine).
2. Go to the folder where the script is located and copy-paste its path.
3. Type: `cd /path/to/script`
4. Press enter.
5. Go to the folder where your music files are located and copy-paste its path.
6. Type: `python rename_by_metadata.py -d /path/to/music/files`
7. Press enter.
