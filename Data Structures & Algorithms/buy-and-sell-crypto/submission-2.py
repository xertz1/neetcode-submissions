class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        largest = prices[0]
        maxProfit = 0  

        for i in range (1, len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
                largest = prices[i]
            
            if prices[i] > largest:
                largest = prices[i]
            
            if largest - smallest > maxProfit:
                maxProfit = largest - smallest 
            
        
        return maxProfit


        