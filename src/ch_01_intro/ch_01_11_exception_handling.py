"""
###########################################################################################
########## Sect 1.11: Exception Handling
###########################################################################################
"""

# There are two types of errors that typically occur:
#     1. syntax error: the programmer has made a mistake in the structure
#        of a statement or expression.
#     2. exception(ie logic/runtime error): logic error leads to a runtime error that causes the 
#        program to terminate. These types of runtime errors are typically called exceptions.

# Catching exceptions:
#   >>>
#       try:
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




