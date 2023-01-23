class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        flag = False
        i = 0
        while not flag and i < len(nums) -1:

            if nums[i] == nums[i+1]:
                flag = True
            i += 1

        print(nums)
        return flag