from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
class SolutionWithCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t)) # True
print(SolutionWithCounter().isAnagram(s, t)) # True