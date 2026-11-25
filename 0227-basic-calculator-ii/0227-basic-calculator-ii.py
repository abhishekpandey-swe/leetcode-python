class Solution:
    @staticmethod
    def _trunc_div(a: int, b: int) -> int:
        q = abs(a) // abs(b)
        return q if (a >= 0) == (b >= 0) else -q

    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"

        # Sentinel "+" forces the last number to be processed
        for ch in s + "+":
            if ch == " ":
                continue

            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack[-1] *= num
                else:  # op == "/"
                    stack[-1] = self._trunc_div(stack[-1], num)

                op = ch
                num = 0

        return sum(stack)