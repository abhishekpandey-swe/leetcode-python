class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        freq = {}
        
        # 'right' expands our window one character at a time
        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1
            
            # If our rule is violated, shrink the window from the left
            while freq[char] > 2:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1  # Move the left rope forward
                
            # Once valid, calculate the current window size and update max_len
            current_window_size = right - left + 1
            max_len = max(max_len, current_window_size)
            
        return max_len