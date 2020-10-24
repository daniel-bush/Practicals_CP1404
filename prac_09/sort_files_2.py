"""Sort files into categories."""

import os

def main():

    file_extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in file_extension_to_category:
            category = input("What category would you like to put {} files into? ".format(extension))
            file_extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

main()