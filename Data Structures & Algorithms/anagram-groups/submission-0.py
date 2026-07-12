class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[frozenset[tuple[str, int]], List[str]] = {}

        for word in strs:
            digest = Counter(word)
            key = frozenset(digest.items())

            if key not in groups.keys():
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
