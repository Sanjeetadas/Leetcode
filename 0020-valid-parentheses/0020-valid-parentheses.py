class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for ch in s:

            # Push opening brackets
            if ch in "({[":
                stack.append(ch)

            # Check closing brackets
            else:
                if not stack:
                    return False

                top = stack.pop()

                if (
                    (ch == ')' and top != '(') or
                    (ch == '}' and top != '{') or
                    (ch == ']' and top != '[')
                ):
                    return False

        # Stack should be empty
        return len(stack) == 0
        