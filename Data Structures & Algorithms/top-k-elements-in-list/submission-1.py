class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        freqList = [[] for i in range(len(nums) + 1)]
        for n, count in freq.items():
            freqList[count].append(n)
        
        i = len(freqList) - 1
        res = []
        while len(res) < k:
            if freqList[i]:
                res += freqList[i]
            i -= 1
        
        return res