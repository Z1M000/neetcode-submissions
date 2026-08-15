class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate thru the array
        # get diff = target - num
        # if diff dne in the map, store map[num] = index
        # if diff exists in the map, return current index and map[diff]
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[num] = i

        
        return [-1, -1]