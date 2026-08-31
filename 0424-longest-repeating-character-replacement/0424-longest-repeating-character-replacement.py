class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequency = {}
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):

            frequency[s[right]] = frequency.get(s[right], 0) + 1

            max_frequency = max(
                max_frequency,
                frequency[s[right]]
            )

            while (right - left + 1) - max_frequency > k:
                outgoing = s[left]
                frequency[outgoing] -= 1
                left += 1

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length