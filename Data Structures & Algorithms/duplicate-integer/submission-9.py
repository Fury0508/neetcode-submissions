class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashNum = {}
        if len(nums) ==0:
            return False
        for num in nums:
            if num in hashNum:
                hashNum[num] +=1
            else:
                hashNum[num] = 1
        val = max(hashNum.values())
        if val >1:
            return True
        return False
