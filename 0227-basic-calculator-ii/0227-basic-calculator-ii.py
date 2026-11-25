class Solution:
    @staticmethod
    def _trunc_div(a: int, b: int) -> int:
        q = abs(a) // abs(b)
        return q if (a >= 0) == (b >= 0) else -q

    def calculate(self, s: str) -> int:
        total = 0   # sum of completed terms
        term = 0    # current term (product/division chain)
        num = 0     # current number
        op = "+"    # previous operator

        # Sentinel "+" forces the last number to be processed
        for ch in s + "+":
            if ch == " ":
                continue

            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                if op == "+":
                    total += term
                    term = num
                elif op == "-":
                    total += term
                    term = -num
                elif op == "*":
                    term *= num
                else:  # op == "/"
                    term = self._trunc_div(term, num)

                op = ch
                num = 0

        return total + term