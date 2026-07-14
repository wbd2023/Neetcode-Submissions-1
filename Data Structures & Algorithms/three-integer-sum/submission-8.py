class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        nums.sort()
        index = 0

        while index < len(nums) - 2:
            left, right = index + 1, len(nums) - 1

            while left < right:
                total = nums[index] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[index], nums[left], nums[right]])

                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

            index += 1
            while index < len(nums) - 2 and nums[index] == nums[index - 1]:
                index += 1

        return results
