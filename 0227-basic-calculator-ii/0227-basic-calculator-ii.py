class Solution:
    @staticmethod
    def _trunc_div(a: int, b: int) -> int:
        q = abs(a) // abs(b)
        return q if (a >= 0) == (b >= 0) else -q

    def calculate(self, s: str) -> int:
        # ---- Tokenize ----
        tokens = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
            elif s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                tokens.append(num)
            else:
                tokens.append(s[i])
                i += 1

        # ---- Pass 1: collapse * and / ----
        values = [tokens[0]]
        i = 1
        while i < len(tokens):
            op, rhs = tokens[i], tokens[i + 1]
            if op == "*":
                values[-1] *= rhs
            elif op == "/":
                values[-1] = self._trunc_div(values[-1], rhs)
            else:
                values.append(op)
                values.append(rhs)
            i += 2

        # ---- Pass 2: evaluate + and - ----
        ans = values[0]
        i = 1
        while i < len(values):
            op, rhs = values[i], values[i + 1]
            ans += rhs if op == "+" else -rhs
            i += 2

        return ans