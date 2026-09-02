class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c+=1
                if c>1:
                    return False
        if nums[-1]>nums[0] and c==1:
            return False
        else:
            return True
                

        