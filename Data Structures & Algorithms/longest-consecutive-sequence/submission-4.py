class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        maxLen = 0 

        for n in nums:
            count = 1
            check = n 
            if (check - 1) not in num: 
                while (check + 1) in num:
                    check += 1
                    count += 1

            if count > maxLen:
                maxLen = count
        
        return maxLen 


        

        
        
        

        