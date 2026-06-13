class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(1) space complexity since there's at most 26 characters (constant) in each counter.
        return Counter(s) == Counter(t)
