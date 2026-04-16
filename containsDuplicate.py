from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    lookup = set()

    for num in nums:
        if num in lookup:
            return True
        lookup.add(num) #add num to the set if found for the first time

    return False


nums = [1,1,1,1,1,4,1,1,2,1,1,7,1,1,1,1,1]

print(containsDuplicate(nums))