class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
def main():
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t)) # True