class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(arr, sum):
            partition=1
            total=0

            for num in arr:
                if total+num <= sum:
                    total+=num
                else:
                    partition+=1
                    total=num
            return partition
        
        mini=max(nums)
        maxi=sum(nums)
        ans=mini

        while mini<=maxi:
            mid=(mini+maxi)//2

            partition=check(nums, mid)

            if partition<=k:
                ans= mid
                maxi=mid-1
            else:
                mini=mid+1
        
        return ans