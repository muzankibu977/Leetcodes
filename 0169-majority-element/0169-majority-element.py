class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct=el=0
        for num in nums:
            if ct==0:
                ct=1
                el=num
            elif num==el:
                ct+=1
            else:
                ct-=1
        r=nums.count(el)
        if r>(len(nums)//2):
            return el
        return -1

        