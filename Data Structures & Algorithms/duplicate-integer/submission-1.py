class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap: pair the number with its count
        # use get(key, 0) to access the count
        # iterate thru the array, if the count is 0, we add 1
        # if the count is 1, it means the number appears at least 2 time, return true
        # if we scan thru the array without returning true, return false

        # dictionary = {}

        # for num in nums:
        #     count = dictionary.get(num, 0)
        #     if count == 0:
        #         dictionary[num] = 1
        #     if count == 1:
        #         return True
        
        # return False

        # use a set. if we have seen it, return True. if not, add it to the set

        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        
        return False












