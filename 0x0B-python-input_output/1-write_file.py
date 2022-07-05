#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """"write file"""
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)


nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
