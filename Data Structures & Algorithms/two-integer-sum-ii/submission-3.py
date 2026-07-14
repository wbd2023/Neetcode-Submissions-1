class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:  # The two indices must refer to different elements.
            total = numbers[left] + numbers[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]  # Convert to 1-based indices.

        raise ValueError("The problem guarantees exactly one solution.")
