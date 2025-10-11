# classic paldindrome, not much to say here

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alpha characters
        clean = ''.join(ch.lower() for ch in s if ch.isalnum())
       

        if len(clean) == 1:
            return True

        # palindromes cannot be odd
        mid = len(clean) // 2
        p1 = 0
        p2 = 0
        for i in range(mid):
            p1 = i
            p2 = -(i+1)
            
            if(clean[p1] != clean[p2]):
                return False
            if i == mid:
                return True
        return True
