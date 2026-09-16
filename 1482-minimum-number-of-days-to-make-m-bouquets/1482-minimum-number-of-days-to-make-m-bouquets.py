class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def pos(bloomDay, day, m, k):
            count=0
            bq=0
            for flowers in bloomDay:
                if flowers<=day:
                    count+=1
                    if count==k:
                        bq+=1
                        count=0
                    else:
                        continue
                else:
                    count=0
            return bq>=m

        if m*k> len(bloomDay):
            return -1

        low=min(bloomDay)
        high=max(bloomDay)
        ans=0

        while low<=high:
            mid=(low+high)//2

            if pos(bloomDay, mid, m, k):
                ans= mid
                high=mid-1
            else:
                low=mid+1
        return ans  
        