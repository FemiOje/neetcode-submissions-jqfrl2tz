class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        while top <= bottom:
            middle = top + (bottom - top) // 2
            
            if matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][-1] < target:
                top = middle + 1
            else:
                break
        
        if top > bottom: return False

        l, r = 0, len(matrix[middle])
        while l <= r:
            mid = l + (r - l) // 2

            if matrix[middle][mid] > target:
                r = mid - 1
            elif matrix[middle][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False


