"""
###########################################################################################
########## Sect 1.12: Defining Functions
###########################################################################################
"""
import random

# def infinite_monkey(target: str, tries: int) -> str:
#     """
#     INPUT
#     target_sentence: sentence to attempt at randomly generating
#     tries: number of tries to try and guess target_sentence
#     OUTPUT
#     closest match to target_sentence
#     """
#     if tries <= 0:
#         raise RuntimeError("Cannot have less than one try")
# 
#     CHOICES ="abcdefghijklmnopqrstuvwxyz "
#     MAX_COUNT = len(target)
# 
#     current_guess = random.choices(CHOICES, k=len(target))
#     best_guess = [0] * len(target)
#     correct_so_far = [0] * len(target)
#     max_correct = 0
#     num_tries = 1
#     while num_tries < tries:  #  RUN TRIALS
#         curr_correct = 0
#         for i in range(len(target)):  # CALCULATE SCORE
#             if current_guess[i] == target[i].lower():
#                 correct_so_far[i] = current_guess[i]
#                 curr_correct += 1
#         if curr_correct > max_correct:
#             max_correct = curr_correct
#             best_guess = current_guess
#         if curr_correct == len(target):  # SUCCESS
#             print("You reached the correct guess!!")
#             print(f"TARGET: {target}")
#             print(f"ACTUAL: {"".join(current_guess)}")
#             print(f"It took {num_tries} tries")
#             break
#         else:  # KEEP TRYING
#             for i in range(len(target)):
#                 if not best_guess[i]:
#                     best_guess[i] = 
#     max_score = max_correct/len(target) * 100

def random_string(str_len: int) -> str:
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz ", k=str_len))

def guess_score(target_str: str, test_str: str) -> float:
    correct_count = 0
    for i in range(len(target_str)):
        if test_str[i] == target_str[i]:
            correct_count += 1
    return correct_count/len(target_str) * 100

def best_guess_after_tries(target_str, num_tries):
    max_score = 0
    best_guess = "0" * len(target_str)
    for i in range(num_tries):
        curr_guess = random_string(len(target_str))
        curr_score = guess_score(target_str, curr_guess)
        if curr_score > max_score:
            max_score = curr_score
            best_guess = curr_guess
        i += 1
        if curr_score == 100:
            print(f"CONGRATULATIONS! You reached the target string after {i} tries")

    print(f"TARGET: {target_str}")
    print(f"BEST GUESS: {best_guess}")
    print(f"SCORE: {max_score}")


if __name__ == "__main__":
    best_guess_after_tries("jazmin velez", num_tries = 10000000000)
