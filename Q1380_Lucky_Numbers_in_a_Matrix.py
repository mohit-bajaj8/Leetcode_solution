#TC:O(3 * m * n) ~ O(m * n)
#SC:O(m + n)

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_list = []
        max_list = []
        for i in range(0, len(matrix)):
            min_val = float("inf")
            for j in range(0, len(matrix[0])):
                if min_val > matrix[i][j]:
                    min_val = matrix[i][j]
            min_list.append(min_val)

        for i in range(0, len(matrix[0])):
            max_val = float("-inf")
            for j in range(0, len(matrix)):
                if max_val < matrix[j][i]:
                    max_val = (matrix[j][i])
            max_list.append(max_val)

        result = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == min_list[i] and matrix[i][j] == max_list[j]:
                    result.append(matrix[i][j])

        return result