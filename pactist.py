import os
import shutil

path = 'test.txt'

try:
    os.remove(path)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("you dont have permission to delete this file")
except OSError:
    print("that folder contains files")
else:
    print(path + "was deleted")