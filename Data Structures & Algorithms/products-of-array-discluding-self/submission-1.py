class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff = [0] * len(nums) 
        pre = [0] * len(nums)
        output = [0] * len(nums)

        total = 0

        for i in range(1,len(nums)):
            if (i - 1 == 0):
                suff[i] = nums[i-1]
                total = nums[i-1]
            else:
                total = total * nums[i-1]
                suff[i] = total
        
        for j in range(len(nums) - 2, -1, -1):
            if (j + 1 == len(nums) - 1):
                pre[j] = nums[j + 1]
                total = nums[j + 1]
            else:
                total = total * nums[j + 1]
                pre[j] = total
            
        
        for x in range(0, len(nums)):
            if (x == 0 or x == len(nums) - 1):
                output[x] = suff[x] + pre[x]
            else:
                output[x] = suff[x] * pre[x]

        return output

        

        




        
            


        