class Solution:
    def isPalindrome(self, s: str) -> bool:
         """
         Approach : Two Pointers - shrink from both ends,
         skip non-alphanumeric characters, compare case-insensitively.

         Time Complexity : O(n) - each character visited at most once.
         Space Complexity : O(1) - only two integer pointer used

         Example:
         Input s = " A man, a plan, a canal: Panama"
         Output : True
        """

         left = 0
         right = len(s) - 1

         while left < right :
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False 

            left += 1
            right -= 1

         return True
                
                
        
