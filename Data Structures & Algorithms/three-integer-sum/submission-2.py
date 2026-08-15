class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        res = []
        nums.sort()

        # loop thru each element and use two pointers to find the second and third element on its right
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
        
        return res
            