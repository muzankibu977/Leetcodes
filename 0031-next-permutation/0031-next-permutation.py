class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)-1
        pivot=-1
        for i in range(n,0,-1):
            if nums[i-1]<nums[i]:
                pivot=i-1
                break
        if pivot==-1:
            nums.reverse()
        else:
            for j in range(n, pivot, -1):
                if nums[j]>nums[pivot]:
                    nums[j], nums[pivot]=nums[pivot],nums[j]
                    break
            nums[pivot+1:]=reversed(nums[pivot+1:])
        