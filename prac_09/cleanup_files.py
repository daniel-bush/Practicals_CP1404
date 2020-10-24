import shutil
import os


def main():
    # change directory to 'Christmas'
    os.chdir('Lyrics/Christmas')
    #
    # # Print a list of all files in current directory
    # print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # rename file to new name - in place
        # os.rename(filename, new_name)



def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name



    # for filename in filenames:
    #     full_name = os.path.join(directory_name, filename)
    #     new_name = os.path.join(directory_name, get_fixed_filename(filename))
    #     os.rename(full_name, new_name)

main()