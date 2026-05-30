class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_freq = {}
        for st in strs:
            freq = {}
            for s in st:
               freq[s] = freq.get(s, 0) + 1
            st_new = tuple(sorted(st))
            if st_new not in hash_freq:
                hash_freq[st_new] = []
            hash_freq[st_new].append(st)
        return list(hash_freq.values())
     