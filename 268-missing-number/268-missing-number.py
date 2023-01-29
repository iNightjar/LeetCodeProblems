class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lenght = len(nums)
        maxSumOfElements = int((lenght*(lenght+1)/2))
        sum = 0
        for iterator in nums:
            sum += iterator
        return maxSumOfElements - sum