class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        numbers = set(nums)
        for num in numbers:
            if num - 1 in numbers:
                continue

            chained = 0
            while num + chained in numbers:
                chained += 1

            longest = max(chained, longest)

        return longest
