class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        for i, num in enumerate(nums):
            if num in freq:
                if abs(i - freq[num]) <= k:
                    return True 
                else:
                    freq[num] = i
            else:
                freq[num] = i
        return False


            
            