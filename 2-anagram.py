# check if given two strings are anagram
# s = "racecar", t = "carrace"
# these two are anagrams.
# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.

"""
Time : O(m + n)
Space : O(m + n)
"""
def is_anagram(s1, s2):
    s1map = {}
    for i in s1:
        if i in s1map:
            s1map[i] = s1map[i] + 1
        else:
            s1map[i] = 1

    s2map = {}
    for j in s2:
        if j in s2map:
            s2map[j] = s2map[j] + 1
        else:
            s2map[j] = 1

    return s1map == s2map

"""
Time : O(mlogm + nlogn)
Space : O(m + n)
"""
def is_anagram_1(s1, s2):
    return sorted(s1) == sorted(s2)


# Uncommnet below to enable testing.

# Testing
"""
import logging
import sys
import random
import string

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def generate_anagram(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def generate_non_anagram(word, change_ratio=0.3):
    word_list = list(word)
    num_changes = max(1, int(len(word) * change_ratio))
    indices = random.sample(range(len(word)), num_changes)
    for i in indices:
        word_list[i] = random.choice(string.ascii_lowercase.replace(word_list[i], ''))
    return ''.join(word_list)

def generate_test_cases(n=20):
    test_cases = []

    for i in range(n):
        base_word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 10)))

        if i % 2 == 0:
            # Positive: generate true anagram
            other = generate_anagram(base_word)
            expected = True
        else:
            # Negative: generate non-anagram
            other = generate_non_anagram(base_word)
            expected = False

        test_cases.append((base_word, other, expected))

    return test_cases

# Example usage

if __name__ == "__main__":
    test_cases = generate_test_cases()

    failure = None
    for i, (s1, s2, expected) in enumerate(test_cases, 1):
        logging.debug(f"Test Case {i}:")
        logging.debug(f"  String 1: {s1}")
        logging.debug(f"  String 2: {s2}")
        actual = is_anagram(s1, s2)
        res = "Pass" if actual==expected else "Fail"
        if res == 'Fail':
            failure = True
            logging.error('Failed')
            logging.error(f"  Result : {res}, Expected: {expected} Actual: {actual}\n")
            sys.exit()
        else:
            logging.debug(f"  Result : {res}, Expected: {expected} Actual: {actual}\n")
    
    
    for i, (s1, s2, expected) in enumerate(test_cases, 1):
        logging.debug(f"Test Case {i}:")
        logging.debug(f"  String 1: {s1}")
        logging.debug(f"  String 2: {s2}")
        actual = is_anagram_1(s1, s2)
        res = "Pass" if actual==expected else "Fail"
        if res == 'Fail':
            failure = True
            logging.error('Failed')
            logging.error(f"  Result : {res}, Expected: {expected} Actual: {actual}\n")
            sys.exit()
        else:
            logging.debug(f"  Result : {res}, Expected: {expected} Actual: {actual}\n")

    logging.info("All passed")
"""



