"""
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
"""

def isValid(s: str) -> bool:
    d = {'(' : ')', '{' : '}', '[': ']'}
    if len(s) == 1:
        return False
    stack = []
    for c in s:
        if c in d:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if d[stack.pop()] != c:
                return False

    return len(stack) == 0

assert isValid("()") == True
assert isValid("(){}[]") == True
assert isValid("(])") == False
assert isValid("([])") == True
assert isValid("(") == False