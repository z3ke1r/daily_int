

class Solution:
    def longestPalindrome(self, s):
        r = []  
        t = []

        for i in range(len(s)):
            if s[i] is s[len(s) - 1 - i]:
                r.append(s[i])
            else:
                if len(r) > len(t):
                    t = r
                    r.clear
        return t
    


# Test program
s = "tracecarst"
print(str(Solution().longestPalindrome(s)))
# racecar
