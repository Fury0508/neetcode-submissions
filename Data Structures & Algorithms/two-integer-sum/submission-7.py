class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for key,value in enumerate(nums):
            n[value] = key 
        for key, value in enumerate(nums):
            second = target - value
            if second in nums and n[second] != key:
                return [key, n[second]]
        return []

