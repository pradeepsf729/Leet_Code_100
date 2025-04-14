"""
Given an integer array nums, return an array answer 
such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums 
is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time 
and without using the division operation.
"""
"""
Time : 
Space :
"""
def productExceptSelf(nums):
    total_product = 1
    zero_val_index = None
    all_zeros = False
    for ind, i in enumerate(nums):
        if i != 0:
            total_product *= i
        else:
            if zero_val_index is not None:
                all_zeros = True
            zero_val_index = ind
            continue

    for i in range(len(nums)):
        if all_zeros:
            nums[i] = 0
        elif zero_val_index is not None:
            if nums[i] == 0:
                nums[i] = total_product
            else:
                nums[i] = 0
        else:
            nums[i] = total_product //  nums[i]
    
    return nums


def prod_prefix_postfix(nums):
    res = [1] * len(nums)
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(len(nums) - 2, -1, -1):
        postfix[i] = postfix[i+1] * nums[i+1]

    for i in range(len(nums)):
        res[i] = prefix[i] * postfix[i]
    
    return res



def test_alg(productExceptSelf):
    ip = [1,2,3,4]
    print(ip)
    res = productExceptSelf(ip)
    print(res)

    print("-------- --------")

    ip = [-1,1,0,-3,3]
    print(ip)
    res = productExceptSelf(ip)
    print(res)

    print("-------- --------")
    ip = [-1,1,0,0,-3,3]
    print(ip)
    res = productExceptSelf(ip)
    print(res)

    print("-------- --------")
    ip = [0,0]
    print(ip)
    res = productExceptSelf(ip)
    print(res)

    print("-------- --------")
    ip = [0,4, 0]
    print(ip)
    res = productExceptSelf(ip)
    print(res)

    print("-------- --------")
    ip = [0, 2, 3 , 4]
    print(ip)
    res = productExceptSelf(ip)
    print(res)


# test_alg(productExceptSelf=productExceptSelf)

test_alg(prod_prefix_postfix)

