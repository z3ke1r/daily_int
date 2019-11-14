"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    - Open brackets are closed by the same type of brackets.
    - Open brackets are closed in the correct order.
    - Note that an empty string is also considered valid.
"""

class Solution:
  def isValid(self, s):
    # Fill this in.
    stack = []
    parentheses = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for i in range(len(s)):
        if s[i] in parentheses:
            if stack[len(stack)-1] is parentheses[s[i]]:
                stack.pop()
        else:
            stack.append(s[i])
    
    if not len(stack):
        return True
    return False

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "([{}])()[]{[]"
# should return False
print(Solution().isValid(s))