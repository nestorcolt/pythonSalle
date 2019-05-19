import maya.cmds as mc

######################################################################################################
# Resources:

# Espanol
# http://elclubdelautodidacta.es/wp/2012/12/python-funciones-para-ricos-y-funciones-para-pobres/
#
# English
# https://www.w3schools.com/python/python_functions.asp

######################################################################################################
# Dictionaries
#
my_dictionary = {}

# Create some key:values
#
my_dictionary["letters"] = "abcdefghijklmnopqrstuvwxyz"
my_dictionary["numbers"] = [0,1,2,3,4,5,6,7,8,9]
my_dictionary["inner_dict"] = {"letters_list": ["a", "b", "c", "d"], "magic_number": 18990129}

######################################################################################################
# output dictionary data
#
print("dict key -> 'letters': {}".format(my_dictionary["letters"]))
print("dict key -> 'numbers': {}".format(my_dictionary["numbers"]))
print("dict key -> 'inner_dict': {}".format(my_dictionary["inner_dict"]))

######################################################################################################
# Indexing dictionary data
#
print("dict value -> string index: {} -> {}".format(0, my_dictionary["letters"][0]))
print("dict value -> list index: {} -> {}".format(1, my_dictionary["numbers"][1]))
print("dict value -> inner dict: {} -> {}".format("magic_number", my_dictionary["inner_dict"]["magic_number"]))

"""
# Note
If parsed key doesn't exists in the dictionary, this will return a 'key error'
"""

######################################################################################################
# listing objects in maya scene

all_objects_in_scene = mc.ls("*")
print("all objects in maya file: {}".format(all_objects_in_scene))
#
object_type = "nurbsCurve"
by_object_type = mc.ls(type=object_type)
print("specific type: {} ".format(by_object_type))
#

######################################################################################################
# iterating over objects list

for item in all_objects_in_scene:
    print(item)

# add some conditions
visibility_value = 0
for item in all_objects_in_scene:
    if mc.objectType(item, isType="nurbsCurve"):
        mc.setAttr("{}.lodVisibility".format(item), visibility_value)
        print(item)

######################################################################################################
# functions (encapsulation) -- (SCOPES)

def print_greetings(magic_name="", english=False):
    if english:
        print("Hey there, my name is {}, and I'm learning python".format(magic_name))
    else:
        print("Hola, mi nombre es {}, y estoy aprendiendo python".format(magic_name))

# function call
print_greetings(magic_name="Nestor", english=False)

"""
Functions make code reusable, code less develop more
"""
######################################################################################################
# toggle visibility by object type

def toggle_visibility(object_list=[], object_type="transform", vis_value=0):
    for item in object_list:
        if mc.objectType(item, isType=object_type):
            mc.setAttr("{}.lodVisibility".format(item), vis_value)

# function call
toggle_visibility(object_list=all_objects_in_scene, object_type="transform", vis_value=1)

######################################################################################################
# create offset / root in objects for parsed list (rigging)

def create_root_group(array=[], create_control=False, parent=False):
    for obj in array:
        raw_name = obj
        #
        if "_" in obj:
            raw_name = "_".join(obj.split("_")[:-1])

        offset = mc.createNode("transform", n="{}_OFFSET".format(raw_name))
        root = mc.createNode("transform", n="{}_ROOT".format(raw_name))
        mc.parent(offset, root)
        #
        mc.matchTransform(root, obj)

        if create_control:
            control = mc.circle(n="{}_CTL".format(raw_name))
            mc.matchTransform(control, obj)
            mc.parent(control, offset)
            mc.parentConstraint(control, obj, mo=True)
        else:
            mc.parent(obj, offset)

        if parent:
            obj_parent = mc.listRelatives(obj, p=True)
            par = ""
            if obj_parent:
                par = obj_parent[0]
                new_parent = "_".join(par.split("_")[:-1]) + "_CTL"
                mc.parent(root, new_parent)

# function call
selection = mc.ls(selection=True)
create_root_group(array=selection, create_control=True)

######################################################################################################
