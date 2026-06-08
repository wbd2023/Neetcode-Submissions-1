class Solution:
    # We want the max `value` that is smaller than `h`.
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return int(math.inf)

        low = 1
        high = max(piles)

        best = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            # Note: `value` and `mid` are inversely proportional
            value = sum(map(lambda x: math.ceil(x / mid), piles))

            print(f"low={low}, high={high}, mid={mid}, value={value}")

            if value > h:
                low = mid + 1
                continue

            # If value <= h.
            high = mid - 1

            if mid < best and value >= sum(map(lambda x: math.ceil(x / best), piles)):
                best = mid

        return best
