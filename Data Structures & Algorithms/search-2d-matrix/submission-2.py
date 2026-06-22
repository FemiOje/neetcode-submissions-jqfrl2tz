class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) - 1

            while l <= r:
                m = l + (r - l) // 2
                curr = matrix[i][m]
                
                if target == curr:
                    return True
                elif target < curr:
                    r = m - 1
                elif target > curr:
                    l = m + 1
        
        return False
        