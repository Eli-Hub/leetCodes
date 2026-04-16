from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    lookup = set(nums1)
    result = set()

    for num in nums2:
        if num in lookup:
            result.add(num)

    return list(result)


nums1 = [1,1,1,1,1,4,1,1,2,1,1,7,1,1,1,1,1]
nums2 = [2,2,2,2,2,5,2,2,2,2,2,8,2,2,2,2,2]

print(intersection(nums1, nums2))