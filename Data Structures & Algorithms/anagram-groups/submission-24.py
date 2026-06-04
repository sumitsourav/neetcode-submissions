class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_freq = {}
        for word in strs:
            freq = {}
            for char in word:
                freq[char] = freq.get(char, 0) + 1
            word_f = tuple(sorted(freq.items()))
            if word_f not in hash_freq:
                hash_freq[word_f] = []
                hash_freq[word_f].append(word)
            else:
                hash_freq[word_f].append(word)
        return list(hash_freq.values())
             



