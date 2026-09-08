class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        numset=set(nums)
        longest=1
        for num in numset:
            if num-1 not in numset:
                count=1
                x=num
                while x+1 in numset:
                    count+=1
                    x+=1
                longest=max(longest, count)
        return longest