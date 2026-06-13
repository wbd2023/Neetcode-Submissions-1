class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1

        # Iterate from right to left through list.
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right                   # Set current to max on right of current.
            max_right = max(max_right, current)  # Update current max on right of current.

        return arr
