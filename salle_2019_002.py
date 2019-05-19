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
    elif content is None:
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

# Test what we know so far ...
#
def store_scene_object_transformation(object_list=[], os_path='', file_name=''):
    pos_data = get_objects_matrix(object_list)
    json_format = json.dumps(pos_data, separators=(',', ':'), indent=4)

    if not os.path.exists(os_path):
        try:
            os.makedirs(os_path)
        except:
            sys.stdout.write("Error: couldn't create path")
            return

    # if path exists or creation successful save the file
    save_file(path=os_path, file_name="{}.json".format(file_name), content=json_format)


def restore_scene_object_transformation(os_path='', file_name=''):
    data = read_file(path=os_path, file_name="{}.json".format(file_name))
    obj_pos_data = json.loads(data)
    set_objects_matrix(obj_pos_data)

######################################################################################################
# do it!
all_transform = mc.ls(type="transform")
PATH = os.path.join(USER_PROFILE, "Documents", "maya", "positionLib")
FILE_NAME = "scene_001"
store_scene_object_transformation(object_list=all_transform, os_path=PATH, file_name=FILE_NAME)
#
#
restore_scene_object_transformation(os_path=PATH, file_name=FILE_NAME)

######################################################################################################
# Part II : Maya commands UI development
#
def ui_initialize(data_path = ""):
    if not data_path or not os.path.exists(data_path):
        mc.error("There is a problem with the path provided, please check it and try again")
        return

    def on_save(widget=""):
        all_transform = mc.ls(type="transform")
        file_name = mc.textField(widget, q=True, text=True)
        #
        if not file_name:
            return
        #
        store_scene_object_transformation(object_list=all_transform, os_path=data_path, file_name=file_name)
        mc.textField(widget, edit=True, text="")

    def on_load(widget=''):
        current_item = mc.optionMenu(widget, q=True, value=True)
        if not current_item:
            return
        #
        file_name = current_item.replace(".json", "")
        restore_scene_object_transformation(os_path=PATH, file_name=file_name)


    win_name = "Sample_window"

    if mc.window(win_name, exists=True):
        mc.deleteUI(win_name)

    window = mc.window(win_name, title="Scene Snapshot Tool", sizeable=True, width=400, retain=False, resizeToFitChildren=True)
    layout = mc.columnLayout(adjustableColumn=True, parent=window, rowSpacing=15)
    mc.text(label="Path To Store Data:", p=layout, align="left", font="boldLabelFont")
    mc.textField(p=layout, text=data_path, editable=False)
    mc.text(label="Save Version:", p=layout, align="left", font="boldLabelFont")
    ver_widget = mc.textField(p=layout, editable=True)
    save_btn = mc.button("Save", parent=layout, command=lambda x: on_save(widget=ver_widget))
    #
    opt_menu = mc.optionMenu("UI_version_loader_menu", w=250, label="Load Version:", parent=layout)

    for item in os.listdir(data_path):
        mc.menuItem(label=item, p=opt_menu)

    load_btn  = mc.button("Load", parent=layout, command=lambda x: on_load(widget=opt_menu))

    # show the UI window now
    mc.showWindow(window)

ui_initialize(data_path=PATH)

######################################################################################################
