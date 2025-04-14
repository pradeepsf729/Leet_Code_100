"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

"""
Time : O(n + u log u)
Space: O(u + k)

n : numbner of elements
u : number of unuique elements
k : top elements to return.
"""
def top_k_frequent(nums : list, k : int):
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    res = sorted(d, key= lambda x: d[x], reverse=True)
    return res[: k]


"""
Time : O(n)
Space: O(n)
bucket sort algorithm
"""
from collections import Counter
def tok_k_frequent_1(nums: list, k: int):
    freq = Counter(nums)

    print(freq)
    buckets = [[] for _ in range(len(nums) + 1)]
    for i, v in freq.items():
        buckets[v].append(i)

    print(buckets)
    res = []
    for i in range(len(buckets) -1, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res

res  = tok_k_frequent_1([1,2,2,3,3,3], 2)
print(res)

res  = tok_k_frequent_1([7, 7], 1)
print(res)
