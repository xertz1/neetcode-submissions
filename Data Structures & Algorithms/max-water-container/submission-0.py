class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max = 0 

        while l < r: 
            if heights[l] > heights[r]:
                if max < heights[r] * (r - l):
                    max = heights[r] * (r - l)
                    print(str(l) +  " " + str(r) + " " + str(heights[r]) + str(max))
                r -= 1
            else:
                if max < heights[l] * (r - l):
                    max = heights[l] * (r - l)
                    print(str(l) +  " " + str(r) + " " + str(max))
                l += 1
            
            print(max)
            
        return max

        