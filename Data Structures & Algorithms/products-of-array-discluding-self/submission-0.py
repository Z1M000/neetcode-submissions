class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prevProduct = 1
        # left product
        for n in nums:
            res.append(prevProduct)
            prevProduct *= n
            # print("prevProduct", prevProduct)
        # right product
        prevProduct = 1
        # print("prevProduct set to 1")
        for i in range(len(res)-1, -1, -1):
            res[i] *= prevProduct
            prevProduct *= nums[i]
            # print("prevProduct", prevProduct)

        return res
        