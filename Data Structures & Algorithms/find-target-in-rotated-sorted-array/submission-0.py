class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # in left sorted array
        # if mid < target, left = mid
        # if mid > target
        #       if left < target, right = mid
        #       if left > target, left = mid

        # in right sorted array
        #  if mid < target: flip everything
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else: 
                    r = mid - 1
            
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1

          
        

        