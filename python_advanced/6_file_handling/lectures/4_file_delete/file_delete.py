import os

try:
    os.remove("delete_me.txt")
except FileNotFoundError:
    print("File already deleted!")
