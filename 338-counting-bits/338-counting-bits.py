class Solution:
    def countBits(self, n) -> list[int]:
        dp_dynamic = [0] * (n + 1)
        offset = 1
        for iterator in range(1, n + 1):
            if offset * 2 == iterator:
                offset = iterator
            dp_dynamic[iterator] = 1  + dp_dynamic[iterator - offset]
        return dp_dynamic