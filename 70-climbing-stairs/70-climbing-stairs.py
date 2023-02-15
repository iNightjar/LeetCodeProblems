class Solution:
    def climbStairs(self, number: int) -> int:
        firstVal, secondVal = 1,1
        for iterator in range(number -1):
            temVal = firstVal
            firstVal = firstVal + secondVal
            secondVal = temVal
        return firstVal