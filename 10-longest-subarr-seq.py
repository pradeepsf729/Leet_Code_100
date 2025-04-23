"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

"""
Time :
Space :
"""
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]

    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix
        


strs = ["flower","flow","flight"]
longestCommonPrefix(strs)


strs = ["dog","racecar","car"]
longestCommonPrefix(strs)

strs = ["a"]
longestCommonPrefix(strs)

strs = ["a", "a"]
longestCommonPrefix(strs)

strs = ["interspecies", "interstellar", "interstate"]
print(longestCommonPrefix(strs))  # Output: "inters"

strs = ["throne", "throne"]
print(longestCommonPrefix(strs))  # Output: "throne"

strs = ["throne", "dungeon"]
print(longestCommonPrefix(strs))  # Output: ""

strs = ["prefix", "prefixes", "prefixation"]
print(longestCommonPrefix(strs))  # Output: "prefix"

strs = ["", "b", "c"]
print(longestCommonPrefix(strs))  # Output: ""

strs = ["a", ""]
print(longestCommonPrefix(strs))  # Output: ""

strs = ["abc", "abc", "abc"]
print(longestCommonPrefix(strs))  # Output: "abc"