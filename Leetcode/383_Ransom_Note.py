from collections import Counter
class Solution:
    # use dict, add if mag has stuff,
    # find quick way of verifying and then leave?
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_mag = Counter(magazine)
        counter_note = Counter(ransomNote)
        
        ransomSet = set(ransomNote)  # can't decide if this makes it faster or not...
        
        for letter in ransomSet:
            if letter not in counter_mag or counter_note[letter] > counter_mag[letter]:
                return False
        return True
