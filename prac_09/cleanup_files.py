import shutil
import os


def main():
    # change directory to 'Christmas'
    os.chdir('Lyrics/Christmas')

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # ignore directories
        if os.path.isdir(filename):
            continue
        get_fixed_filename(filename)

        # new_name = get_fixed_filename(filename)
        # print("Renaming {} to {}".format(filename, new_name))

        # rename file to new name - in place
        # os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    print("Processing", filename)
    # change " " to _ and .TXT to .txt
    temp_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    i = 0
    index_list = []
    for char in temp_name:
        if i != 0:
            if char.isupper() and temp_name[i-1].islower():
                index_list.append(i)
        i += 1
    print(index_list)
    new_word = []
    iteration = 1
    for number in index_list:
        if iteration = 1:
            where_from = 0:

        where_from = i
        where_to = index_list[i]
        new_word.append(temp_name[where_from:where_to])
        new_word.append("_")
    print(new_word)


    """I have spend hours on this and I have NO IDEA - recording not available of prac to help me!! """

    # for change in range(1, number_of_changes):
    #     print(change)





    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    # return new_name



    # for filename in filenames:
    #     full_name = os.path.join(directory_name, filename)
    #     new_name = os.path.join(directory_name, get_fixed_filename(filename))
    #     os.rename(full_name, new_name)

main()