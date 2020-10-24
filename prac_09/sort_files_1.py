"""Sort files based on attempt.
Daniel Bush
"""

import os


def main():
    """Main function for sorting files."""

    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        file_extension = filename.split('.')[-1]
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        print("{}/{}".format(file_extension, filename))
        os.rename(filename, "{}/{}".format(file_extension, filename))



main()
