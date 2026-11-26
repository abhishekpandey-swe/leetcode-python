class Solution:
    def canAliceWin(self, n: int) -> bool:

        alice_turn = True
        required = 10
        stones = n 


        while stones >= required:
            stones -= required 
            required -= 1

            alice_turn = not alice_turn

        return not alice_turn 
        