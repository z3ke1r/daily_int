

class Solution:

    def lcs(self, s, t):
        m = len(s)
        n = len(t)
        matrix = [[0 for x in range(n + 1)] for y in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] is t[j-1]:
                    matrix[i][j] = 1 + matrix[i-1][j-1]
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

        return matrix[m][n]

    def longestPalindrome(self, s):

        t = ""
        for i in range(len(s) - 1, -1, -1):
            t = t + s[i]

        print(s,t)
        r = self.lcs(s,t)

        return r


# Test program
s = "tracecarst"
print(str(Solution().longestPalindrome(s)))
# racecar
