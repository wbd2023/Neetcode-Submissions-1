class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1

        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            first = matrix[mid][0]

            print(f"checking row {mid}, first={first}")

            if first <= target:
                row = mid          # this row could contain target
                low = mid + 1      # try to find a later possible row
            else:
                high = mid - 1     # target must be in an earlier row

        print(f"chosen row = {row}")

        if row == -1:
            return False

        low = 0
        high = len(matrix[row]) - 1

        while low <= high:
            mid = (low + high) // 2
            value = matrix[row][mid]

            print(f"checking matrix[{row}][{mid}] = {value}")

            if value < target:
                low = mid + 1
            elif value > target:
                high = mid - 1
            else:
                return True

        return False

def debug(**kwargs) -> None:
    print(", ".join(f"{name}={value!r}" for name, value in kwargs.items()))
