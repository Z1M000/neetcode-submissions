class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for n in nums:
            if (n-1) not in numsSet:
                temp = 0
                while n in numsSet:
                    n += 1
                    temp += 1
                res = max(res, temp)
        
        return res
                


        