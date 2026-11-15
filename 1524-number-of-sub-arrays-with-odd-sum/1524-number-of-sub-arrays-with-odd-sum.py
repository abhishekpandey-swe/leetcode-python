class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7

        even_count = 1
        odd_count = 0
        
        prefix = 0
        ans = 0

        for x in arr:
            prefix += x

            if prefix % 2 == 0:
                ans += odd_count
                even_count += 1

            else:
                ans += even_count
                odd_count += 1

            ans %= MOD

        return ans


        