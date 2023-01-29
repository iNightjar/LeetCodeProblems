class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        lenght = len(nums)
        # print(lenght)
        for iterator in range(len(nums)):
            if (iterator != nums[iterator]):
                return iterator
            if (nums[lenght-1] != lenght):
                return lenght