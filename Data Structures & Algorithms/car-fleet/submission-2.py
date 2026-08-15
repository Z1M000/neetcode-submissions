class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (position, speed) pairs
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
        # sort decreasingly based on position
        pairs.sort(reverse = True)
        # caculate each car's time to get to the destination, push it into the stack
        # if it costs more then the prev car
        for p, s in pairs:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        
        # return the length of the stack
        return len(stack)