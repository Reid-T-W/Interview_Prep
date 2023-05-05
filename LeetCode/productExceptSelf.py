#!/usr/bin/env python3
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = [1 for _ in range(len(nums))]
    suffix = [1 for _ in range(len(nums))]
    product_except_self = [1 for _ in range(len(nums))]
    # populating prefix
    for ind in range(len(nums) - 1):
        prefix[ind + 1] = prefix[ind] * nums[ind]
    # populating suffix
    for ind in range(1, len(nums)):
        suffix[len(nums) - 1 - ind] = suffix[len(nums) - ind] * nums[len(nums) - ind]
    
    # return the product of suffix and prefix
    for i in range(len(nums)):
        product_except_self[i] = prefix[i] * suffix[i]
    return product_except_self






nums = [1,2,3,4]
print(productExceptSelf(nums))