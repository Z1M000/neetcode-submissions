class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def robOne(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob2, rob1 + n)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        res = max(nums[0], robOne(nums[:-1]), robOne(nums[1:]))
        return res