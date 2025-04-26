
"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
Find two numbers such that they add up to a specific target number.

Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. 
Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. 
Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. 
Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

"""

"""
def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1

    while j > i:
        curSum = numbers[i] + numbers[j]
        if curSum == target:
            return [i+1, j+1]
        elif curSum < target:
            i += 1
        elif curSum > target:
            j -= 1

    # for two elements case
    return [1, 2]

class TestTwoSumSorted():
    def assertEqual(self, ips, a, b):
        if a != b:
            raise AssertionError(f"Input - {ips}, Expected {a} but got {b}")
        
    def test_example_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(numbers, twoSum(numbers, target), [1, 2])

    def test_example_2(self):
        numbers = [2, 3, 4]
        target = 6
        self.assertEqual(numbers, twoSum(numbers, target), [1, 3])

    def test_example_3(self):
        numbers = [-1, 0]
        target = -1
        self.assertEqual(numbers, twoSum(numbers, target), [1, 2])

    def test_large_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 19
        self.assertEqual(numbers, twoSum(numbers, target), [9, 10])

tester = TestTwoSumSorted()
tester.test_example_1()
tester.test_example_2()
tester.test_example_3()
tester.test_large_numbers()

print("All tests passed!")