#!/usr/bin/python3
"""
write_file function
"""


def append_write(filename="", text=""):
    """Write into file , create if it doesn't exit"""
    with open(filename, 'a', encoding=("utf8")) as file:
        num_c = file.write(text)
        return num_c


nb_characters_added = append_write(
    "file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
