"""
A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. 

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

"""
Time : O(n)
Space : O(n)
"""
#is_palindrome("A man, a plan, a canal: Panama")

import re
def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        
        if not s[j].isalnum():
            j -= 1
            continue

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True
    

res = is_palindrome("A man, a plan, a canal: Panama")
assert res == True

res = is_palindrome("race a car")
assert res == False

res = is_palindrome(" ")
assert res == True

res = is_palindrome("race  ecar")
assert res == True