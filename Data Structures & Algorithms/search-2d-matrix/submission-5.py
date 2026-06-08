class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value < target:
                low = mid + 1
            elif value > target:
                high = mid - 1
            else:
                return True

        return False


def debug(**kwargs) -> None:
    print(", ".join(f"{name}={value!r}" for name, value in kwargs.items()))
