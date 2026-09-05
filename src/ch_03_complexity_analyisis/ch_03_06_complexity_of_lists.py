"""
###########################################################################################
########## Sect 3.6: Complexity Analysis of Lists 
###########################################################################################
* The most common operations on lists are indexing and assigning to an index position, and
  both of these operations have O(1) time complexity

* Another common operation is to grow a list, and there are two ways to do this:
    1. append method ie append()  -->  O(1)
    2. Concatenation operator ie +  -->  O(k), where k is size of list that is being concatenated

* Sample results for timing tests in __main__:
> concat  6.54352807999 milliseconds
> append  0.306292057037 milliseconds
> comprehension  0.147661924362 milliseconds
> list range  0.0655000209808 milliseconds    <- FASTEST by at least one order of magnitude

* contains operation on lists is O(n) whereas average performance of contains on dicts is O(1)
"""
from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


if __name__ == "__main__":
    t1 = Timer("test1()", "from __main__ import test1")
    print("concat ",t1.timeit(number=100000), "milliseconds")

    t2 = Timer("test2()", "from __main__ import test2")
    print("append ",t2.timeit(number=100000), "milliseconds")

    t3 = Timer("test3()", "from __main__ import test3")
    print("comprehension ",t3.timeit(number=100000), "milliseconds")

    t4 = Timer("test4()", "from __main__ import test4")
    print("list range ",t4.timeit(number=100000), "milliseconds")

