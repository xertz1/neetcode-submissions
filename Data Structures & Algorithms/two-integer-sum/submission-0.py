class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_dict = {}
        arr = []

        for i in range (0, len(nums)):
            if target - nums[i] in my_dict:
                arr = [my_dict[target-nums[i]], i]
            
            my_dict[nums[i]] = i
        
        return arr 

        
        