class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        temp=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                if c>temp:
                    temp=c
            else:
                c=0
        return temp

        