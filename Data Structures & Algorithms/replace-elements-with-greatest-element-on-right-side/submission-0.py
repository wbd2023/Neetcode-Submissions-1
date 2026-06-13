class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_right = max(arr[i + 1 :]) if i + 1 < len(arr) else -1
            arr[i] = max_right

        return arr
