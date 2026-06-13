class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        repeats = 2
        ans = []

        for _ in range(repeats):
            for num in nums:
                ans.append(num)

        return ans
