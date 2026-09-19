class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for k,v in enumerate(nums):
            left = target - v
            if left in seen:
                return [seen[left],k]
            seen[v] = k
        