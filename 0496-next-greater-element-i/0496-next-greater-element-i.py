class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        map_stack={}
        for num in reversed(nums2):
            while stack and num>=stack[-1]:
                stack.pop()
            map_stack[num]= stack[-1] if stack else -1
            stack.append(num)
        
        return [map_stack[val] for val in nums1]
        