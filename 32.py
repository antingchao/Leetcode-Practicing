# https://leetcode.com/problems/longest-valid-parentheses/description/
# 32. Longest Valid Parentheses

# reference: https://leetcode.com/problems/longest-valid-parentheses/solutions/5373015/stack-solution-video-explanation/
# using stack to store the index of waiting '('

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # using stack to store the index of waiting '('
        # fill the value -1 to avoid confusion with index values (values >= 0).
        stack = [-1] 
        
        maxLen = 0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else: # s[i] == ')'
                stack.pop()
                if len(stack)==0: # previous recorded one is ')', not matched
                    stack.append(i)
                else: # '(' and ')' matched, update maxLen if the new len is bigger
                    maxLen = max(maxLen, i-stack[-1])
        return maxLen
