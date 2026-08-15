class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def recur(n, memo = None):
            if memo is None:
                memo = {}
            
            if n in memo:
                return memo[n]
            
            if n == 0: return 0
            elif n == 1: return nums[0]
            elif n == 2: return max(nums[0], nums[1])
            
            # print("current memo", memo)
            rob_last = recur(n-2, memo) + nums[n-1]
            skip_last = recur(n-1, memo)
            memo[n] = max(rob_last, skip_last)

            return memo[n]

        return recur(len(nums))



    # def fibonacci_top_down(n, memo=None):
    #     # Initialize the memo dictionary on the first call
    #     if memo is None:
    #         memo = {}
            
    #     # Check if value was already calculated
    #     if n in memo:
    #         return memo[n]
            
    #     # Base cases
    #     if n <= 1:
    #         return n
            
    #     # Recursive step + storing the result in memo
    #     memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
    #     return memo[n]



        