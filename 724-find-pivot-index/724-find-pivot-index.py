class Solution:
    def pivotIndex(self, nums: List[int]) -> int: # function annotation
        if len(nums) == 0:
            return -1
        leftSum = [0, nums[0]]
        rightSum = [0, nums[-1]]
        for i in range(1, len(nums) - 1):
            # print(nums[i])
            # print(leftSum[-1])
            leftSum.append(nums[i] + leftSum[-1])
            rightSum.append(nums[len(nums)-1-i] + rightSum[-1])
        rightSum = rightSum[::-1]
        print(leftSum)
        print(rightSum)
        for i in range(len(leftSum)):
            if leftSum[i] == rightSum[i]:
                return i
        return -1
