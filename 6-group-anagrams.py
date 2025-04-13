"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

"""

"""

"""
from collections import Counter

ip  = ["eat","tea","tan","ate","nat","bat"]
def groupAnagrams(strs):
    strs1 = [''.join(sorted(s)) for s in strs]
    d = {}
    for i in range(len(strs1)):
        if strs1[i] in d:
            d[strs1[i]].append(i)
        else:
            d[strs1[i]] = [i]
    
    res = []
    for k, v in d.items():
        res.append([strs[x] for x in v])

    return res

ip  = ["eat","tea","tan","ate","nat","bat"]
res = groupAnagrams(ip)
output = [["bat"],["nat","tan"],["ate","eat","tea"]]
print(res)

ip  = [""]
res = groupAnagrams(ip)
output = [""]
print(res)


ip  = ["a"]
res = groupAnagrams(ip)
output  = ["a"]
print(res)




