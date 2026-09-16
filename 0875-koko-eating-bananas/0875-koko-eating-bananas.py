import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def count(piles, speed):
            totalh = 0
            for bananas in piles:
                totalh += math.ceil(bananas / speed)
            return totalh

        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            totalh = count(piles, mid)

            if totalh <= h:
                ans = mid
                high = mid - 1 
            else:
                low = mid + 1   

        return ans