class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pt=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=pt[i-1][j-1]+pt[i-1][j]
            pt.append(row)
        return pt
        