class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum=count=0
        prefixsumcount={}
        prefixsumcount[0]=1
        for i in range(len(nums)):
            prefixsum+=nums[i]
            remove=prefixsum-k

            if remove in prefixsumcount:
                count+=prefixsumcount[remove]

            prefixsumcount[prefixsum]=prefixsumcount.get(prefixsum, 0)+1
        return count