class Solution:
    def isPalindrome(self, s: str) -> bool:
         """
        Problem:
            Determine whether the given string is a valid palindrome
            after ignoring non-alphanumeric characters and case.

        Args:
            s (str): Input string.

        Returns:
            bool:
                True  -> if the string is a palindrome.
                False -> otherwise.

        Time Complexity: O(n)
        Reason:
            - Each character is visited at most once.
            - The left and right pointers only move toward the center.
            - No character is processed more than once.

        Space Complexity: O(1)
        Reason:
            - Only two integer pointers (left and right) are used.
            - No additional data structure proportional to the input size
              is created.
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
                
                
        