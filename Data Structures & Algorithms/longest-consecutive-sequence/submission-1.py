class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            streak,current=0,n
            while current in set(nums):
                streak+=1
                current+=1
            res=max(res,streak)
        return res