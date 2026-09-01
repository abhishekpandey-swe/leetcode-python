class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        target_frequency = {}
        for char in p :
            target_frequency[char] = (target_frequency.get(char, 0) + 1)

        result = []
        current_frequency = {}
        left = 0
        matches = 0
        required_matches = len(target_frequency)

        for right in range(len(s)):
            incoming = s[right]

            # Remove the old relationship.
            if incoming in target_frequency:
                if current_frequency.get(incoming , 0) == target_frequency[incoming]:
                    matches -= 1 

            # Add incoming character.
            current_frequency[incoming] = current_frequency.get(incoming, 0) + 1

            # Check new relationship.
            if incoming in target_frequency :
                if current_frequency[incoming] == target_frequency[incoming]:
                    matches += 1

            # Maintain fixed window size = len(p)
            if right - left + 1 > len(p):
                outgoing = s[left]

                # Removing the old matching relationship.
                if outgoing in target_frequency:
                    if current_frequency[outgoing] == target_frequency[outgoing]:
                        matches -= 1

                # Removing outgoing character.
                current_frequency[outgoing] -= 1

                # Check new relationship.
                if outgoing in target_frequency:
                    if current_frequency[outgoing] == target_frequency[outgoing]:
                        matches += 1

                left += 1

            if matches == required_matches:
                result.append(left)

        return result



             





        