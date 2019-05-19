import maya.cmds as mc
import os
import sys
import json

######################################################################################################
# Resources:

# Espanol
# http://elclubdelautodidacta.es/wp/tag/os/
# https://programacion.net/articulo/como_trabajar_con_datos_json_utilizando_python_1403
#
# English
# https://docs.python.org/3/library/os.path.html
# https://www.w3schools.com/python/python_json.asp
######################################################################################################

# os module
#

"""
We're gonna focus on:

os.path.join()
os.path.exists()
os.makedirs()
os.listdir()

"""

# joining paths with os.path.join
ROOT_PATH = os.environ["USERPROFILE"]
print("operative system user root path: {} ".format((ROOT_PATH)))
#
JOINED_PATH = os.path.join(ROOT_PATH, "documents", "screenshots")
print("joined path: {} ".format((JOINED_PATH)))

# check if a path exists with os.path.exists
print(os.path.exists(JOINED_PATH))
#
DOCUMENTS_FOLDER = os.path.join(ROOT_PATH, "documents")
print(os.path.exists(DOCUMENTS_FOLDER))

# creating directories
if not os.path.exists(JOINED_PATH):
    # check if path doesn't exist, then create path
    os.makedirs(JOINED_PATH)

# listing a directory
DIR_FOLDERS = os.listdir(DOCUMENTS_FOLDER)

for item in DIR_FOLDERS:
    print(item)

######################################################################################################
# open read/write files with python & functions return
#
# Creating a path and saving a .txt file
USER_PROFILE = os.environ["USERPROFILE"]
PATH = os.path.join(USER_PROFILE, "Documents", "maya")

def save_file(path="",file_name="", content=None):
    if not os.path.exists(path):
        sys.stdout.write("Error: {} is not a valid path".format(path))
        return
    elif content is  None:
        sys.stdout.write("Error: content to save is empty")
        return

    file_path = os.path.join(path, file_name)
    with open(file_path, "w") as writer:
        writer.write(content)


def read_file(path, file_name=""):
    if not os.path.exists(path):
        sys.stdout.write("Error: {} is not a valid path".format(path))
        return

    file_path = os.path.join(path, file_name)
    with open(file_path, "r") as reader:
        data = reader.read()
        return data


# Calling functions
#
# save
dummy_content = "This is a test, of what you can do with os module.\nTry it out by yourself.\n\n2019"
save_file(path=PATH, file_name="dummie.txt", content=dummy_content)

# read
data = read_file(path=PATH, file_name="dummie.txt")
print(data)

######################################################################################################
# serializing files (( JSON ))
# Json allows to encode any python data structure into text to store and work with it cross language

some_data = [1, 2, 3, {'4': 5, '6': 7}]
json_format = json.dumps(some_data, separators=(',', ':'), indent=4)
print(json_format)

read_json = json.loads(json_format)
print(read_json)
#
#
# getting objects with transformations from maya scene

all_transform = mc.ls(type="transform")
print(all_transform)

# get matrix function
def get_objects_matrix(object_list=[]):
    #
    outout_dict = {}
    for object in object_list:
        matrix = mc.xform(object, query=True, worldSpace=True, matrix=True)
        outout_dict[object] = matrix
        #

    return outout_dict


# set matrix function
def set_objects_matrix(object_data={}):
    for object, matrix in object_data.items():
        mc.xform(object,  worldSpace=True, matrix=matrix)
        #

# calling functions
pos_data = get_objects_matrix(all_transform)
set_objects_matrix(pos_data)

######################################################################################################
