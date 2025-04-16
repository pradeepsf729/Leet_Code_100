"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3

"""

def longestConsecutive(nums):
    s = set(nums)
    d = {}
    for i in nums:
        if i - 1 in s:
            pass
        else:
            d[i] = 1

    max_seq = 1
    counter = 1
    for k, v in d.items():
        while k+1 in s:
            counter += 1
            k = k+1

        if counter > max_seq:
            max_seq = counter
        counter = 1
    return max_seq  


ip = [100, 4, 200, 1, 2, 3]
res = longestConsecutive(ip)
assert res == 4

ip = [0,3,7,2,5,8,4,6,0,1]
res = longestConsecutive(ip)
assert res == 9

ip = [1,0,1,2]
res = longestConsecutive(ip)
assert res == 3

ip = [100, 100, 100, 100, 100, 100]
res = longestConsecutive(ip)
assert res == 1

ip = []
res = longestConsecutive(ip)
assert res == 0
