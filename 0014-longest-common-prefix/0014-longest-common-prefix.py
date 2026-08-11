class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        # Sort the array alphabetically
        strs.sort()
        
        # Take the most different strings (first and last)
        first = strs[0]
        last = strs[-1]
        
        prefix = []
        # Compare them character by character
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            prefix.append(first[i])
            
        return "".join(prefix)