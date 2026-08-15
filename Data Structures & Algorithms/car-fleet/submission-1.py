class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            time = (target - p)/s
            # print(p, s, time)
            if not stack or time > stack[-1]:
                stack.append(time)
                # print("appended", time)
        
        return len(stack)
        