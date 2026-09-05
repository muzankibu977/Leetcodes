class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        et=(n*(n+1))//2
        at=sum(nums)
        return et-at
        