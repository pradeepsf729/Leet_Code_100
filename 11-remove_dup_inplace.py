"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, 
you need to do the following things:

Change the array nums such that the first k elements of nums 
contain the unique elements in the order they were present in nums initially. 

The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, 
with the first two elements of nums being 1 and 2 respectively.

It does not matter what you leave beyond the returned k (hence they are underscores).


Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, 
with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.

It does not matter what you leave beyond the returned k (hence they are underscores).
"""

def removeDuplicates(nums):
    i = 0
    j = i + 1
    l = len(nums)
    #print(nums)
    # 0 0 1 1 1 2 2 3 3 4
    # 
    while j < l:
        if nums[i] == nums[j]:
            j = j + 1
        else:
            nums[i+1] = nums[j]
            i = i + 1
            j = j + 1
    #print(nums)
    return nums

# Test cases to call removeDuplicates

# Test case 1: Simple case with duplicates
nums1 = [1, 1, 2]
removeDuplicates(nums1)

# Test case 2: Larger array with multiple duplicates
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
removeDuplicates(nums2)

# Test case 3: Array with no duplicates
nums3 = [1, 2, 3, 4, 5]
removeDuplicates(nums3)

# Test case 4: Array with all elements the same
nums4 = [2, 2, 2, 2, 2]
removeDuplicates(nums4)

# Test case 5: Empty array
nums5 = []
removeDuplicates(nums5)

# Test case 6: Array with one element
nums6 = [7]
removeDuplicates(nums6)





