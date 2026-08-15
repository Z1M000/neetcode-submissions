class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for i in range(len(nums)):
            temp = max(curMin * nums[i], curMax * nums[i], nums[i])
            curMin = min(curMin * nums[i], curMax * nums[i], nums[i])
            curMax = temp
            res = max(res, curMax)
        
        return res
        