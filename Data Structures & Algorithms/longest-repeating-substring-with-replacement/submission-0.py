class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        res = 0
        maxFreq = 0

        for r in range(len(s)):
            # Add the current character to the frequency map
            freq[s[r]] = freq.get(s[r], 0) + 1

            # Keep track of the highest frequency in the current window
            maxFreq = max(maxFreq, freq[s[r]])

            # If more than k replacements are needed, shrink the window
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1

            # Update the longest valid window
            res = max(res, r - l + 1)

        return res
        