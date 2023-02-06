class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        print(set(nums), type(set(nums)))
        print(set(range(1,len(nums)+1 )))
        firstValue = set(range(1,len(nums)+1))
        secondValue = set(nums)
        return list(firstValue - secondValue)