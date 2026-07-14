class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first, second = {"index": 0, "height": heights[0]}, {"index": 1, "height": heights[1]}

        print(heights[2:])

        for index, height in enumerate(heights[2:], start=2):
            print(index, height)
            print(first, second)

            best = self.area(first, second)
            
            candidate = {"index": index, "height": height}

            if self.area(candidate, second) > best and self.area(candidate, second) > self.area(first, candidate):
                first = candidate
                continue

            if self.area(first, candidate) > best and self.area(first, candidate) > self.area(candidate, second):
                second = candidate
                continue

        print(first, second)

        return self.area(first, second)

    @staticmethod
    def area(first: Dict[str, int], second: Dict[str, int]) -> int:
        distance = abs(first["index"] - second["index"])
        height = min(first["height"], second["height"])
        return distance * height
