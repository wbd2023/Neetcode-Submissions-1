class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:                             # Use <, not <=, because the middle character need not be compared with itself.
            while i < j and not s[i].isalnum():
                i += 1

            while j > i and not s[j].isalnum():  # `i` is unchanged, so skip with a while loop instead of restarting with a continue.
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i, j = i + 1, j - 1

        return True
