# Abstract data types
# Encapsulation
# Abstraction
# Data hiding
# Interpreted language
# Object-oriented
# Python interpreter >>>
# An object is an instance of a class

# integer division (//): when two integers are divided, the result 
# is a floating point. The integer division operator returns the integer 
# portion of the quotient by truncating any fractional part.

# A Python variable is created when a name is used for the first time on
# the left-hand side of an assignment statement. Assignment statements 
# provide a way to associate a name with a value. The variable will hold a 
# reference to a piece of data and not the data itself.
                 
# Unordered collections: sets, dictionaries




###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
########## Sect 1.8: Getting Started with Data
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

###########################################################################################
###########################################################################################
########## Sect 1.8.1: Built-In Atomic Data Types 
###########################################################################################
###########################################################################################

###########################################################################################
###########################################################################################
########## Sect 1.8.2: Built-in Collection Data Types
###########################################################################################
###########################################################################################

###########################################################################################
########## SEQUENCES
###########################################################################################
# Ordered collections(ie sequences): strings, arrays, tuples
# ******************************************************
# # OPERATORS SUPPORTED BY ALL SEQUENCES
# ******************************************************
# # indexing []
# concatenation +
# membership in 
# length len
# slicing [:] 
# repetition *  : concatenate a repeated number of times
#   -> used for quick initialization of lists
#      eg   >>> my_list = [0] * 4
#           >>> my_list
#           [0, 0, 0, 0]
#   -> One very important aside relating to the repetition operator is that the
#      result is a repetition of references to the data objects in the sequence.

# >>> my_list = [1, 2, 3]
# >>> my_list.index(2)
# 1
# >>> my_list.index(55)
# ValueError: 55 is not in the list
# my_list.remove(target_val) also throws the same exception when target_val
# is not in the sequence

# index() vs find()
# NOTE: The difference between my_list.index(target) and my_list.find(target) is
# that index() throws a ValueError when the target is not found, while find() returns -1





###########################################################################################
#################### LISTS/ARAYS 
###########################################################################################
# ******************************************************
# METHODS SUPPORTED BY LISTS (in addition to operators suppored by all sequences)
# ******************************************************
# # append
# alist.append(item)
# Adds a new item to the end of a list
# 
# insert
# alist.insert(i,item)
# Inserts an item at the ith position in a list
# 
# pop
# alist.pop()
# Removes and returns the last item in a list
# 
# pop
# alist.pop(i)
# Removes and returns the ith item in a list
# 
# sort
# alist.sort()
# Modifies a list to be sorted
# 
# reverse
# alist.reverse()
# Modifies a list to be in reverse order
#
# del
# del alist[i]
# Deletes the item in the ith position
# 
# index
# alist.index(item)
# Returns the index of the first occurrence of item
# 
# count
# alist.count(item)
# Returns the number of occurrences of item
# 
# remove
# alist.remove(item)
# Removes the first occurrence of item
# >>> j = "jazmin velez"
# >>> j.split("xxx")
# ['jazmin velez']
# >>> j = "jazmin velezxxx"
# >>> j.split("xxx")
# ['jazmin velez', '']





###########################################################################################
########## STRINGS
###########################################################################################
# ******************************************************
# METHODS SUPPORTED BY STRINGS (in addition to operators suppored by all sequences)
# ******************************************************
# center
# astring.center(w)
# Returns a string centered in a field of size w
# 
# count
# astring.count(item)
# Returns the number of occurrences of item in the string
# 
# ljust
# astring.ljust(w)
# Returns a string left-justified in a field of size w
# 
# lower
# astring.lower()
# Returns a string in all lowercase
# 
# rjust
# astring.rjust(w)
# Returns a string right-justified in a field of size w
# 
# find
# astring.find(item)
# Returns the index of the first occurrence of item
# 
# split
# astring.split(schar)
# Splits a string into substrings at schar

# print takes zero or more parameters and displays them using a single blank as the 
# default separator. It is possible to change the separator character by setting the
# sep argument. In addition, each print ends with a newline character by default.
# This behavior can be changed by setting the end argument. 
# print("Hello","World", sep="***")
# Hello***World
# print("Hello","World", end="***")
# Hello World***>>>  # NOTE: No new line





###########################################################################################
########## SETS 
###########################################################################################
# ******************************************************
# A set is an unordered collection of zero or more immutable Python data objects. 
# Sets do not allow duplicates and are written as comma-delimited values enclosed 
# in curly braces. The empty set is represented by set(). Sets are heterogeneous. 
# The empty set is represented by set(). 
# NOTE: if you try to initialize an empty set using {}, it will behave as a dict and NOT a set

# ******************************************************
# OPERATORS SUPPORTED BY SETS(in addition to operators suppored by all collections)
# ******************************************************
# membership
# in
# Set membership
# 
# length
# len
# Returns the cardinality of the set
# 
# |
# aset | otherset
# Returns a new set with all elements from both sets
# 
# &
# aset & otherset
# Returns a new set with only those elements common to both sets
# 
# -
# aset - otherset
# Returns a new set with all items from the first set not in second
# 
# <=
# aset <= otherset
# Asks whether all elements of the first set are in the second

# !!!!!!!!!! Dictionaries and sets are unordered sequences even if they may appear ordered !!!!!!
# A set is an unordered collection of zero or more IMMUTABLE types.
#    -> If a mutable type is added to a set, an error is raised
#       eg >>> a = set()
#          >>> a.add("x")
#          >>> a.add([1,2])
#          Traceback (most recent call last):
#            File "<python-input-5>", line 1, in <module>
#              a.add([1,2])
#              ~~~~~^^^^^^^
#          TypeError: unhashable type: 'list'

# ******************************************************
# METHODS SUPPORTED BY SETS
# ******************************************************
# union
# aset.union(otherset)
# Returns a new set with all elements from both sets
# 
# intersection
# aset.intersection(otherset)
# Returns a new set with only those elements common to both sets
# 
# difference
# aset.difference(otherset)
# Returns a new set with all items from first set not in second
# 
# issubset
# aset.issubset(otherset)
# Asks whether all elements of one set are in the other
# 
# add
# aset.add(item)
# Adds item to the set
# 
# remove
# aset.remove(item)
# Removes item from the set
# 
# pop
# aset.pop()
# Removes an arbitrary element from the set
# 
# clear
# aset.clear()
# Removes all elements from the set





###########################################################################################
########## DICTIONARIES 
###########################################################################################
# ******************************************************
# OPERATORS SUPPORTED BY DICTIONARIES(in addition to operators suppored by all collections)
# *****************
# []
# myDict[k]
# Returns the value associated with k, otherwise its an error
#
# in
# key in adict
# Returns True if key is in the dictionary, False otherwise
#
# del
# del adict[key]
# Removes the entry from the dictionary*************************************

# ******************************************************
# METHODS SUPPORTED BY DICTIONARIES
# ******************************************************
# keys
# adict.keys()
# Returns the keys of the dictionary in a dict_keys object
# 
# values
# adict.values()
# Returns the values of the dictionary in a dict_values object
# 
# items
# adict.items()
# Returns the key-value pairs in a dict_items object
# 
# get
# adict.get(k)
# Returns the value associated with k, None otherwise
# 
# get
# adict.get(k,alt)
# Returns the value associated with k, alt otherwise

###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
########## Sect 1.9: Input and Output
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

# The value returned by input() will always be a string





###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
########## Sect 1.10: Control Structures
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
# Two main control structures:
#   1. Iteration
#      - while loop
#      - for loop
#   2. Selection
#      - if
# example of a nested list comprehension
#   --> USING NESTED LOOPS:
#       wordlist = ['cat','dog','rabbit']
#       letterlist = [ ]
#       for aword in wordlist:
#           for aletter in aword:
#               letterlist.append(aletter)
#       print(letterlist)

#   --> USING CHAINED LIST COMPREHANSION 
#       wordlist = ['cat','dog','rabbit']
#       letterlist = set([letter for word in wordlist for letter in word])
#       print(letterlist)





###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
########## Sect 1.11: Exception Handling
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
# There are two types of errors that typically occur when writing programs:
#     1. syntax error: the programmer has made a mistake in the structure
#        of a statement or expression.
#     2. exception(ie logic/runtime error): logic error leads to a runtime error that causes the 
#        program to terminate. These types of runtime errors are typically called exceptions.

# Catching exceptions:
#   >>>
#   try:
#          print(math.sqrt(anumber))
#       except:
#          print("Bad Value for square root")
#          print("Using absolute value instead")
#          print(math.sqrt(abs(anumber)))
# 
#   Bad Value for square root
#   Using absolute value instead
#   4.79583152331
#   >>>

# Raising custom exceptions:
#   if anumber < 0:
#      raise RuntimeError("You can't use a negative number")
#   else:
#      print(math.sqrt(anumber))
#   
#   Traceback (most recent call last):
#     File "<stdin>", line 2, in <module>
#   RuntimeError: You can't use a negative number
#   >>>




###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
########## Sect 1.12: Defining Functions
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

# Classes can be organized into hierarchies.

# A class constructor should always invoke the constructor of its parent before 
# continuing on with its own data and behavior.

# LEFT OFF HERE





###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
########## Sect 1.13: OOP in Python: Defining Classes
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################





# GENERAL NOTES:
# lambda functions
# map, filter, zip functions
#    -> zip produces a "list" of tuples that has length equal to the minimum length of
#       the iterables passed in 
# callback functions
# tuple unpacking, *args, **kwargs
# sort by key

if __name__ == "__main__":
    pass