class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        best = current

        for num in nums:
            current = current + 1 if num else 0
            best = max(best, current)

        return best
