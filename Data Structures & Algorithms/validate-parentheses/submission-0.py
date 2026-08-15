class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            print(p)
            if p in ["(", "[", "{"]:
                stack.append(p)
                # print("appended", p)
                # print("stack", stack)
            elif len(stack) == 0: return False
            elif p == ")" and stack.pop() != "(":
                return False
            elif p == "]" and stack.pop() != "[":
                return False
            elif p == "}" and stack.pop() != "{":
                return False
            # else:
                # print("special case", p)
        
        # print("stack after loop", stack)
        if len(stack) == 0:
            return True
        
        return False
                
        