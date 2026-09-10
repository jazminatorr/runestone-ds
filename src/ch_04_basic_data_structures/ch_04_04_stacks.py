"""
###########################################################################################
########## Sect 4.4 - 4.9: The Stack Abstract Data Type 
###########################################################################################
* Linear Data Structures - collections where once an item is added, it stays in that
position relative to the items that came before and came after it
    -> They can be thought of as having two ends: left/right, top/bottom, front/rear
    -> Linear data structures are distinguished from one another based on the way in which
       items are added and removed, in particular where these additions/removals occur


"""
class MyStack:
    """
    An ordered collection of items where the addition of new items and removal 
    of existing items always takes place at the same end.
    *** Stacks are fundamentally important, as they can be used to reverse the order of items
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


def reverse_string(input_str: str) -> str:
    input_stack = MyStack()
    for char in input_str:
        input_stack.push(char)
    reversed_str = ""
    while not input_stack.isEmpty():
        reversed_str += input_stack.pop()
    return reversed_str

def parens_are_balanced(expression: str) -> bool:
    pass