class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        my_dict = {}

        sec_dict = {}

        for i in range(0, len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = 1
            else:
                my_dict[s[i]] = my_dict[s[i]] + 1
        
        for j in range (0, len(t)):
            if t[j] not in sec_dict:
                sec_dict[t[j]] = 1
            else:
                sec_dict[t[j]] = sec_dict[t[j]] + 1

        if my_dict == sec_dict:
            return True
        else:
            return False
            


        