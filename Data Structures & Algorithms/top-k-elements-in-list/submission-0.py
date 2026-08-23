class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        # build the freq map
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        # print(freq)
        # insert to correponding freq
        freqList = [[] for i in range(len(nums) + 1)]
        # print(freqList)
        for n, count in freq.items():
            freqList[count].append(n)
    
        # walk the list backwards
        i = len(freqList) - 1
        while len(res) < k:
            if freqList:
                res += freqList[i]
            i -= 1
        
        return res
        