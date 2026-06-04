class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_fre = {}

        for st in strs:
            freq = {}

            for s in st:
                freq[s] = freq.get(s, 0) + 1

            key = tuple(sorted(freq.items()))

            if key not in hash_fre:
                hash_fre[key] = []

            hash_fre[key].append(st)

        return list(hash_fre.values())