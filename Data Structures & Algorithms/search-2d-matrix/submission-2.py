class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_low = 0
        row_high = len(matrix) - 1

        while row_low <= row_high:
            row_mid = (row_low + row_high) // 2
            first_value = matrix[row_mid][0]

            debug(
                stage="row search",
                row_low=row_low,
                row_high=row_high,
                row_mid=row_mid,
                first_value=first_value,
            )

            if first_value < target:
                row_low = row_mid + 1
            elif first_value > target:
                row_high = row_mid - 1
            else:
                return True

        chosen_row = row_mid

        debug(
            stage="chosen row",
            chosen_row=chosen_row,
            row_low=row_low,
            row_high=row_high,
            row_mid=row_mid,
        )

        col_low = 0
        col_high = len(matrix[chosen_row]) - 1

        while col_low <= col_high:
            col_mid = (col_low + col_high) // 2
            value = matrix[chosen_row][col_mid]

            debug(
                stage="column search",
                col_low=col_low,
                col_high=col_high,
                col_mid=col_mid,
                value=value,
            )

            if value < target:
                col_low = col_mid + 1
            elif value > target:
                col_high = col_mid - 1
            else:
                return True

        return False


def debug(**kwargs) -> None:
    print(", ".join(f"{name}={value!r}" for name, value in kwargs.items()))