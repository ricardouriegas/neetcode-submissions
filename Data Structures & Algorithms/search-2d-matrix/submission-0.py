class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            left, right = 0, len(i) - 1

            while left <= right:
                mid = (left + right) // 2
                if i[mid] > target:
                    right = mid - 1
                elif i[mid] < target:
                    left = mid + 1
                else:
                    return True

        return False
