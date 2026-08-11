class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0 
        l = 0 
        compareString = set()
        longestLength = 0


        while r != len(s):
            if s[r] not in compareString:
                compareString.add(s[r])
                r += 1

            else:
                compareString.remove(s[l])
                l += 1

            longestLength = max(len(compareString), longestLength)

        return longestLength 


        