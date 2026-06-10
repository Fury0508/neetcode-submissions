class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow] and slow != fast:
                slow+=1
                nums[slow],nums[fast] = nums[fast],nums[slow]
                
                
        return slow +1