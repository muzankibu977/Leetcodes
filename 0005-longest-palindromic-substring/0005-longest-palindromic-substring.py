class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        result=''

        def res(left, right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1: right]
        
        for i in range(len(s)):
            p1= res(i, i)
            p2= res(i, i+1)

            result=max(result, p1, p2, key= len)
        
        return result