class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]

        for i in range(1, len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])

            if s[i] == ")" or s[i] == "]" or s[i] == "}":
                if not stack:
                    return False

            if s[i] == ")":
                if stack.pop() != "(":
                    return False
            if s[i] == "]":
                if stack.pop() != "[":
                    return False

            if s[i] == "}":
                if stack.pop() != "{":
                    return False


        if not stack:
            return True
        else:
            return False