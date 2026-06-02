class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_n = {}

        for i in nums:
            if i in hash_n:
                hash_n[i] +=1
            else:
                hash_n[i] = 1
        for k,v in hash_n.items():
            if v > (len(nums)/2):
                return k