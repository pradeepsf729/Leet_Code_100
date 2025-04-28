"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false


"""

def wordPattern(pattern: str, s: str) -> bool:
    


    l = s.split(" ")

    if len(pattern) != len(l):
        return False
    
    d1 = {}
    d2 = {}
    for i in range(len(pattern)):
        if pattern[i] not in d1:
            if l[i] in d2:
                return False
            d2[l[i]] = pattern[i]
            d1[pattern[i]] = l[i]
        else:
            if d1[pattern[i]] != l[i]:
                return False
    return True

assert wordPattern("abba", "dog cat cat dog") == True
assert wordPattern("abba", "dog cat cat fish") == False
assert wordPattern("abba", "dog cat cat ") == False
assert wordPattern("a", "dog") == True
assert wordPattern("abba", "dog dog dog dog") == False


