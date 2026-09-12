from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0

        def func(nums):
            nonlocal count
            
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = func(nums[:mid])
            right = func(nums[mid:])
            
            # count reverse pairs
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j
            
            return merge(left, right)

        def merge(left, right):
            temp = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    temp.append(left[i])
                    i += 1
                else:
                    temp.append(right[j])
                    j += 1
            
            temp.extend(left[i:])
            temp.extend(right[j:])
            return temp

        func(nums)
        return count