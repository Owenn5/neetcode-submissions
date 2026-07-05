class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        
        for i in range(len(s_sorted)):
            anagram = (True)
            non_anagram = (False)

            if s_sorted[i] != t_sorted[i]:
                return non_anagram
        
        return True