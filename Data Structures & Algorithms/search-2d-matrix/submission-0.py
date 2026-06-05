class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            debug(low=low, high=high, mid=mid)

            if matrix[mid][0] < target:
                low = mid + 1
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                return True

        m = mid
        debug(m=m, low=low, high=high, mid=mid)

        low = 0
        high = len(matrix[m]) - 1

        while low <= high:
            mid = (low + high) // 2
            debug(low=low, high=high, mid=mid)

            if matrix[m][mid] < target:
                low = mid + 1
            elif matrix[m][mid] > target:
                high = mid - 1
            else:
                return True

        # debug(low=low, high=high, mid=mid)
        return False

def debug(**kwargs) -> None:
    print(", ".join(f"{name}={value!r}" for name, value in kwargs.items()))
