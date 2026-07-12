class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequencies = [[] for _ in range(len(nums))]

        for num, frequency in count.items():
            frequencies[frequency - 1].append(num)

        results = []
        for result in frequencies[::-1]:
            if result:
                results.extend(result)

                if len(results) >= k:
                    break

        return results
