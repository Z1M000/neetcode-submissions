class Solution:
    def rob(self, nums: List[int]) -> int:
        def robOne(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        
        return max(nums[0], robOne(nums[1:]), robOne(nums[:len(nums)-1]))