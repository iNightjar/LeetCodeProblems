class NumArray:

    def __init__(self, nums: List[int]):
        sumOfIndex = 0
        self.result = []
        for iterator in nums:
            sumOfIndex += iterator
            self.result.append(sumOfIndex)

    def sumRange(self, left: int, right: int) -> int:
        right = self.result[right]
        left = self.result[left -1] if left > 0 else 0
        return right - left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)