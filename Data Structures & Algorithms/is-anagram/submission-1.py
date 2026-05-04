class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        fir_dict = {}

        sec_dict = {}

        for i in range(len(s)):
            fir_dict[s[i]] = 1 + fir_dict.get(s[i], 0)
            sec_dict[t[i]] = 1 + sec_dict.get(t[i], 0)

        return fir_dict == sec_dict
            
            


        