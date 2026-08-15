class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Greedy + Two Pointer approach.
        
        Always try to pair the lightest available person
        with the heaviest. If they fit together, both board.
        If not, the heaviest goes alone.
        
        Time Complexity  : O(n log n) — due to sorting
        Space Complexity : O(1)       — in-place sort, no extra DS
        """
        people.sort()

        lightest = 0
        heaviest = len(people) - 1
        boats = 0

        while lightest <= heaviest:
            # Can the lightest and heaviest share a boat?
            if people[lightest] + people[heaviest] <= limit:
                lightest += 1   # Both board → move lightest pointer inward

            # Heaviest always boards (alone or with lightest)
            heaviest -= 1
            boats += 1

        return boats