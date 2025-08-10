class Solution:
    # # solution-1: TC:O(N*M*(N+M))+O(N*M) SC:O(1) Most basic solution with worst TC
    # # Worst solution in terms of time complexity.
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if matrix[i][j]==0:
    #                 self.mark(matrix,i,j)
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if matrix[i][j]==float("inf"):
    #                 matrix[i][j]=0

    # def mark(self,matrix,row,col):
    #     r=len(matrix)
    #     c=len(matrix[0])
    #     for i in range(r):
    #         j=col
    #         if matrix[i][j]!=0:
    #             matrix[i][j]=float("inf")
    #     for i in range(c):
    #         j=row
    #         if matrix[j][i]!=0:
    #             matrix[j][i]=float("inf")

    # # solution 2: TC:O(2*N*M)~O(N*M) SC:O(N+M)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowt = [0 for _ in range(len(matrix))]
        colt = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowt[i] = -1
                    colt[j] = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rowt[i] == -1 or colt[j] == -1:
                    matrix[i][j] = 0