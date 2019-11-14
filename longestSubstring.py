class Solution:
    def lengthOfLongestSubstring(self, s):
        ans = []
        lCount = 0
        lSub = 0
        for i in range(len(s)):
            if s[i] not in ans:
                ans.append(s[i])
                lCount += 1
            else:
                if lCount > lSub:
                    lSub = lCount
                lCount = 0
                ans.clear()

        return lSub
                        

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
