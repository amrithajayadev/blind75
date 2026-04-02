class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'(':')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            # if an opening char, then add
            if ch in char_map.keys():
                stack.append(ch)
            # if matching closing char, then pop
            elif stack and char_map.get(stack[-1]) == ch:
                stack.pop()
            # if non-matching closing char, then invalid , return False immediately.
            elif stack and char_map.get(stack[-1]) != ch:
                return False
            # if stack is empty and non opening char is given, return False
            elif not stack and ch not in char_map.keys():
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        