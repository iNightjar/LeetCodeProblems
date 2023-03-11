class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Two pionters problem"""
        rightPointer = 0
        leftPointer = 0
        maxResult = 0
        while rightPointer < len(prices):
            if prices[leftPointer] <= prices[rightPointer]:
                profit = prices[rightPointer] - prices[leftPointer]
                maxResult = max(maxResult, profit)

            else:
                leftPointer = rightPointer
            rightPointer += 1
        return maxResult