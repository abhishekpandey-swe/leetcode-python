class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Approach : Two pointer with one skip - when mismatch 
        found, try skipping either left or right characters.

        Time Complexity : O(n)
        Space Complexity : O(1)

        Example :
        Input s = "abca"
        Output : True(remove 'c' or 'b'
        """
        def is_pal(i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pal(l + 1, r) or is_pal(l, r - 1)
            l += 1
            r -= 1
        return True
