class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=float('-inf')
        cstart=start=end=0
        for i, num in enumerate(nums):
            sum+=num
            if sum>maxi:
                maxi=sum
                start=cstart
                end=i
            if sum<0:
                sum=0
                cstart=i+1
        return maxi
        