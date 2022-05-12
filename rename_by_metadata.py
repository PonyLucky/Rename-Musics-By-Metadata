# This script will rename audio files based on metadata.
# It will get the 'title' metadata from the file and rename the file to that.
# The files are in 'flac' or 'wav' format.


import os
import sys
import argparse
import mutagen
from mutagen.flac import FLAC


def get_args():
    parser = argparse.ArgumentParser(description='Rename audio files based on metadata.')
    parser.add_argument('-d', '--directory', help='Directory to search for files.', required=True)
    return parser.parse_args()

def get_files(directory):
    files = []
    for file in os.listdir(directory):
        if file.endswith('.flac') or file.endswith('.wav'):
            files.append(file)
    return files

def get_metadata(file, directory):
    file_path = directory + '/' + file
    if file.endswith('.flac'):
        metadata = FLAC(file_path)
    elif file.endswith('.wav'):
        metadata = mutagen.File(file_path)
    title = metadata['title']
    # while title is of type list, get the first element
    while isinstance(title, list):
        title = title[0]
    position = metadata['tracknumber']
    # while position is of type list, get the first element
    while isinstance(position, list):
        position = position[0]
    return title, position

def get_extension(file):
    return file.split('.')[-1]

def rename_file(directory, file, new_name):
    os.rename(directory + '/' + file, directory + '/' + new_name)

def display_results(files, directory):
    """
    The results are displayed in a table.
    The length of the table is determined by the longest file name.
    For example:
    +------------------------------------------+
    | original name           | new name       |
    +------------------------------------------+
    | file1.flac              | 1 title.flac   |
    | file2.flac              | 2 title.fla    |
    | file3.flac              | 3 title.flac   |
    +------------------------------------------+
    """
    max_length = 0
    for file in files:
        if len(file) > max_length:
            max_length = len(file)
    # Get the new names
    new_names = []
    for file in files:
        title, position = get_metadata(file, directory)
        extension = get_extension(file)
        new_name = str(position) + ' ' + title + '.' + extension
        new_names.append(new_name)
    # Max length of the new names
    max_length_new_names = 0
    for new_name in new_names:
        if len(new_name) > max_length_new_names:
            max_length_new_names = len(new_name)
    # Print the table
    print('+' + '-' * max_length + '+' + '-' * max_length_new_names + '+')
    print('|' + 'original name'.ljust(max_length) + '|' + 'new name'.ljust(max_length_new_names) + '|')
    print('+' + '-' * max_length + '+' + '-' * max_length_new_names + '+')
    for i in range(len(files)):
        print('|' + files[i].ljust(max_length) + '|' + new_names[i].ljust(max_length_new_names) + '|')
    print('+' + '-' * max_length + '+' + '-' * max_length_new_names + '+')

def confirmation():
    confirmation = input('\nAre you sure you want to rename the files? (y/n) ')
    if confirmation.lower() == 'y':
        return True
    else:
        return False

def main():
    args = get_args()
    directory = args.directory
    files = get_files(directory)
    # Display the results
    display_results(files, directory)
    # Ask for confirmation
    if confirmation():
        for file in files:
            title, position = get_metadata(file, directory)
            extension = get_extension(file)
            new_name = str(position) + ' ' + title + '.' + extension
            rename_file(directory, file, new_name)


if __name__ == '__main__':
    main()