class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            
            # include the current num
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # exclude the current num
            cur.pop() # 撤销这个选择，恢复现场，因为第二个 dfs（exclude）需要的是恢复后的状态
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res
            
        