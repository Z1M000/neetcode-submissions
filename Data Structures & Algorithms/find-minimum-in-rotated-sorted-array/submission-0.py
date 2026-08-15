class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # if first < last: not rotated, return first
        # recursion:
        # base case: high == low: return low
        # get index of high and low, and mid
        # if mid is smaller than low, recur [low, mid]
        # else recur [mid, high]

        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        def recur(low, high):
            print(f"LOW index {low}: {nums[low]}")
            print(f"HIGH index {high}: {nums[high]}")
            if low == high - 1:
                return high 
            
            mid = (low + high) // 2
            print(f"MID index {mid}: {nums[mid]}")
            if nums[mid] < nums[low]:
                return recur(low, mid)
            else:
                return recur(mid, high)

        i = recur(0, len(nums)-1)
        return nums[i]
        
        