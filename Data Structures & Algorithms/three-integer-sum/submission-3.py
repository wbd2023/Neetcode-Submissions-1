class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        nums.sort()
        index = 0

        print(nums)

        while index in range(len(nums)):
            left, right = index + 1, len(nums) - 1

            print(nums[index])

            turns = 0
            while left < right and turns < 6:
                total = nums[index] + nums[left] + nums[right]

                print(left, right)

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    results.append([nums[index], nums[left], nums[right]])

                    left += 1
                    while left - 1 in range(len(nums)) and nums[left] == nums[left - 1]:
                        left += 1

                    right -= 1
                    while right + 1 in range(len(nums)) and nums[right] == nums[right + 1]:
                        right -= 1

                turns += 1

            index += 1
            while index in range(len(nums)) and index - 1 in range(len(nums)) and nums[index] == nums[index - 1]:
                index += 1

        return results
