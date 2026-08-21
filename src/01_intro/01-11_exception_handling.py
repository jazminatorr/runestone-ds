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
