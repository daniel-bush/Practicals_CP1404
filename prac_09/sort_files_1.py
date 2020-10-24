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




main()
