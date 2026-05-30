class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        temp = sorted(s1)
        for char in s1:
            freq[char] = freq.get(char, 0) + 1
        for i in range(len(s2)):
            current_freq = {}
            if s2[i] in temp:
                j = i + 1
                current_freq[s2[i]] = current_freq.get(s2[i], 0) + 1
                while j < len(s2):
                    if s2[j] in temp and freq != current_freq:
                        current_freq[s2[j]] = current_freq.get(s2[j], 0) + 1
                        j = j + 1
                        continue
                    else:
                        break 
                if current_freq == freq:
                    return True
        return False
                
                



                