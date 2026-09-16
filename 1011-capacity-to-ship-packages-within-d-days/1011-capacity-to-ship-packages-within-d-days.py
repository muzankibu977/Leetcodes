class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=0

        while low<=high:
            mid=(low+high)//2

            load=0
            day=1
            for weight in weights:
                load+=weight
                if load<=mid:
                    continue
                else:
                    day+=1
                    load=weight
            if day<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        
        return ans

        