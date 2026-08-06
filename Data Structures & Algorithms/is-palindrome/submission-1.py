class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for c in s:
            if c.isalnum():
                new += c.lower()

        length = len(new)

        for i in range(length // 2):
            j = length - 1 - i
            if new[i] != new[j]:
                return False

        return True
        
        