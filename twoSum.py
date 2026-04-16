import math
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]: # type: ignore
    for i, val_i in enumerate(nums):
        for j, val_j in enumerate(nums[i+1:], i+1):
            if val_i + val_j == target:
                return [i, j]



nums = [1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1]
target = 11
print(twoSum(nums, target))