class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for index, value in enumerate(nums):
            complement = target - value

            if value in complements.keys():
                return [complements[value], index]

            complements[complement] = index
