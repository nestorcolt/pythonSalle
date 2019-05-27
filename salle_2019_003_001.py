# Review Lesson
# Operation over string - list and dictionaties


# -------------------------------------------------------------------------------------------------
string_example = "aveces caminamos juntos"
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

# strings --------------------------------------------------------------
# replace string
replaced_word = string_example.replace("aveces", "siempre")
#
control_name = "L_upperArm_01_CTL"
joint_name = control_name.replace("_CTL", "_JNT")

# startswith
if control_name.startswith("L_"):
    print(True)
else:
    print(False)

# endswith
if control_name.endswith("_JNT"):
    print(True)
else:
    print(False)

# lower - uppper - capitalize
print(control_name)
print(control_name.upper())
print(control_name.lower())
#
print(control_name.capitalize())
print(string_example.title())
#
print(string_example.isupper())
print(string_example.islower())
print("longitud de data: {}".format(len(string_example)))
#
# methodos de listas

print("longitud de data: {}".format(len(lista)))

# append & insert
lista.append("word")
print(lista)
lista.insert(-1, "end")
print(lista)

# pop & remove
elemento = lista.pop(5)
print(elemento)
lista.remove("end")
print(lista)

#
try:
    lista.remove("casa")
except:
    print("the item you've tried to delete was not in this data container")

# zfill()
control_name = "L_upperArm_{}_CTL".format(001)
print(control_name)

control_name = "L_upperArm_{}_CTL".format(str(10).zfill(3))
print(control_name)

# incremental version name
for index in range(10):
    version_name = "control_version_{}".format(str(index).zfill(3))
    print(version_name)

#
# list --------------------------------------------------

# reverse list
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(lista)

# reversed list - modifies the same data structure
lista.reverse()
print(lista)
#
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
duplicated_list = lista[:] # make a copy from a list filtering items with the slicing (non destructive way)
duplicated_list.reverse()
print(lista)
print(duplicated_list)

# index of (return index of element passed to method index())
print(lista.index("d"))

# sorting elements inside of a list
numbers = [9,5,3,7,8,6,4,2,1,0]
print(numbers)
numbers.sort()
print numbers
#
abc = ["d", "c", "a", "b"]
abc.sort()
print(abc)
#
abc = ["d", "c", "a", "b", "?", "D", 0, "5"]
abc.sort()
print(abc)

# sorted list
abc = ["d", "c", "a", "b"]
sorted_abc = sorted(abc)
print(abc)
print(sorted_abc)

for letter in sorted_abc:
    print(letter)

# min - max
numbers = [9,5,3,7,8,6,4,2,1,0]
#
print(max(numbers))
print(min(numbers))

# min - max
abc = ["d", "c", "a", "b"]
#
print(max(abc))
print(min(abc))

#
# --------------------------------------------------------------------------
# empty:
my_dictionary = {}
