"""
###########################################################################################
########## Sect 1.10: Control Structures
###########################################################################################
"""

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

### LIST COMPREHENSIONS

def perfect_squares(n: list) -> list:
    """
    create a list of the first 10 perfect squares
    """
    squares = [x**2 for x in range(n)]
    print(squares)
    print(type(squares))
    return(squares)

def letters_in_wors_list(word_list):
    """
    returns a list of all of the unique letters in a list of words
    """
    pass

if __name__ == "__main__":
    perfect_squares(10)


