def is_annagram_01(target_str: str, other_str: str) -> bool:
    """
    Take two strings as input and determine if they are annagrams of each other. 
    One string is an annagram of another if they ininclude the same exact chars 
    regardless of the order of those chars. This solution assumes both strs are
    of the SAME LENGTH.
    """
    if len(target_str) != len(other_str):
        return False
    other_list = list(other_str.lower())
    is_annagram = True
    for char in target_str:
        found = False
        for i in range(len(other_list)):
            if char.lower() == other_list[i]:
                found = True
                other_list[i] = None
                break  # break from inner loop, found matching char in the other string
        if not found:
           is_annagram = False
           break  # break from outer loop, there is a char in target_str that is not in the other
    return is_annagram


def is_annagram_02(target_str: str, other_str: str) -> bool:
    is_annagram = True
    if len(target_str) != len(other_str):
        return False
    return sorted(target_str.lower()) == sorted(other_str.lower())


def is_annagram_03(target_str: str, other_str: str) -> bool:
    """
    generate a list of all possible annagrams of target_str and check if other_str is one of them
    Complexity Analysis: O(n!)
    """
    pass  # TODO: Finish if you feel like it, don't want to use this IRL

def is_annagram_04(target_str: str, other_str: str) -> bool:
    NUM_OF_LETTERS_IN_ALPHABET = 26
    target_char_count = [0] * NUM_OF_LETTERS_IN_ALPHABET
    other_char_count = [0] * NUM_OF_LETTERS_IN_ALPHABET

    for i in range(len(target_str)):
        counter_position = ord(target_str[i].lower()) - ord('a')
        target_char_count[counter_position] += 1

    for i in range(len(other_str)):
        counter_position = ord(other_str[i].lower()) - ord('a')
        other_char_count[counter_position] += 1

    is_annagram = True
    for i in range(NUM_OF_LETTERS_IN_ALPHABET):
        if target_char_count[i] != other_char_count[i]:
            is_annagram = False
            break
        else:
            continue
    return is_annagram

