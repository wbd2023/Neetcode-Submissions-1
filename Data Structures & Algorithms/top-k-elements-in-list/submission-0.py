class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        
        result = []
        for _ in range(k):
            best_key = -1
            best_value = -1

            for key, value in frequencies.items():
                if value <= best_value:
                    continue

                best_key = key
                best_value = value

            frequencies.pop(best_key)
            result.append(best_key)

        return result
