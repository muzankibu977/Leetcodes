class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        temp=[0]*(len(nums))
        pind=0
        nind=1
        for num in nums:
            if num>0:
                temp[pind]=num
                pind+=2
            else:
                temp[nind]=num
                nind+=2
        return temp
        