from string import ascii_lowercase

# Review Lesson
# Operation over string - list and dictionaries

string_var = "sometimes we walk together"
list_var = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

# indexing / slicing review
print(string_var[5])
print(list_var[5])

#
print(string_var[0:9])
print(list_var[2:-1])


# strings --------------------------------------------------------------
# replace string
replaced_word = string_var.replace("sometimes", "always")
#
control_name = "L_upperArm_CTL"
joint_name = control_name.replace("_CTL", "_JNT")
print(control_name, joint_name)

# startswith
check = control_name.startswith("L_")
#
if check:
    print(True)
else:
    print(False)

# endswith
if control_name.endswith("CTL"):
    print(control_name)
else:
    print(False)

# lower - upper - capitalize - title
print(control_name)
print(control_name.lower())
print(control_name.upper())
#
print(string_var.capitalize())
print(string_var.title())

#
alpha = "abc"
digits = "123456789"
print(string_var.islower())
print(string_var.isupper())
print(control_name.isalpha())
print(digits[0].isdigit())
print(len(string_var))
print("data length: {}".format(len(string_var)))

# zfill(X) add "0" zeros to the left of a number as many X specified in function call
mesh = "C_geometryDummy_{}_MSH".format(str(1).zfill(3))
print(mesh)

for index in range(1, 101):
    name = "C_geometryDummy_{}_MSH".format(str(index).zfill(3))
    print(name)

# --------------------------------------------------------------------------
# list methods
# append & insert
print("data length: {}".format(len(list_var)))

# filling list
new_list = []
print(new_list)
#
new_list.append("newItems") # append a new element at the end of the list
print(new_list)
new_list.insert(2, "insertedItem") # insert a new element at the given index of the list

# pop & remove
abc_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(abc_list)
letter = abc_list.pop(0)
print(letter)
#
abc_list.remove("b")
print(abc_list)

try:
    abc_list.remove("HOME")
except:
    print("the value entered couldn't be found")

#

# reverse list
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(lista)
lista.reverse()
print(lista)

copied_list = lista[:]
print(copied_list)
del copied_list[:]
print(copied_list)
print(lista)

# index of (return index of element passed to method index(X))
print(lista.index("d"))

# sorting elements inside of a list
numbers = [9,5,3,7,8,6,4,2,1,0]
print(numbers)
numbers.sort()
print numbers

#
# sorted list
abc = ["d", "c", "a", "b"]
sorted_abc = sorted(abc)
print(abc)
print(sorted_abc)


# min - max
numbers = [9,5,3,7,8,6,4,2,1,0,-1]
#
print(max(numbers))
print(min(numbers))

# min - max
abc = ["d", "c", "a", "b"]
#
print(max(abc))
print(min(abc))

# --------------------------------------------------------------------------
# Dictionaries

# empty:
my_dictionary = {}

# fill a dict
my_dictionary["clave"] = "value"
print(my_dictionary)


# iterate over a list and fill dict with data
new_dict = {}
print(ascii_lowercase)

for idx, letter in enumerate(ascii_lowercase): # enumerate returns a index number with current iteration
    new_dict[letter] = idx


print(new_dict)

for key, val in new_dict.items():
    print("Letter: {} -- IndexValue: {}".format(key, val))

# accessing to elements from a dictionary
j_letter_index =  new_dict["j"]
print(j_letter_index)

#
get_j_letter_index = new_dict.get("j", None)
print(get_j_letter_index)

# getting non existent elements in a dict
any_value = new_dict["A"] # error if key doesn't exist in dictionary (stop code execution)
print(any_value)

any_value = new_dict.get("A", None) # return what has been passed as second argument if key doesn't exists
print(any_value)
#
if any_value is None:
    print(False)

# -------------------------------------------------------

# Functions and Returns
def add_int(a=0, b=0):
    try:
        result =  a + b
        return result
    #
    except:
        print("Hey smart pants what you are trying to do is invalid.")
        return False
#
sumNums = add_int(15.897, "5")
print(sumNums)

# ---------------------------------------------------------
# concatenation
# string concatenation

string_001 = "L" + "_" + "arm" + "_" + "CTL"
print(string_001)
#
#
upperArmControl = "L_upperArm" + "_CTL"
print(upperArmControl)
#
arm = 'upperArm'
prefix = 'L'
suffix = 'CTL'

# option 1
armControlName = prefix + "_" + arm + "_" + suffix
print(armControlName)


# option 2 (** RECOMENDED **)
armControlName = "{}_{}_{}".format(prefix, arm, suffix)
print(armControlName)

# option 3
armControlName = "_".join([prefix, arm, suffix])
print(armControlName)

####################
# List concatenation
abc_001 = ["a", "b", "c", "d"]
abc_002 = ["e", "f", "g", "h"]

concatenated_list = abc_001 + abc_002
print(concatenated_list)
#
concatenated_list = abc_002 + abc_001
print(concatenated_list)
concatenated_list.sort()
print(concatenated_list)

# ------------------------------------------------------------------------------------------
# sorting, concatenating and enumerating list in a for loop
upper_letters = []
lower_letters = []

for letter in sorted(abc_002 + abc_001):
    upper_letters.append(letter.upper())
    lower_letters.append(letter)

print(upper_letters)
print(lower_letters)

#
print(len(upper_letters), len(lower_letters))

# we cant iterate over two list at the same time with zip python build-in function. check this out
for low, up in zip(lower_letters, upper_letters):
    print("lowercase: {} --- uppercase: {}".format(low, up))



# enumerate + zip (freaking this out a bit)
for index, (low, up) in enumerate(zip(lower_letters, upper_letters)):
    print("index: {} -- lowercase: {} --- uppercase: {}".format(index, low, up))


# ------------------------------------------------------------------------------------------
