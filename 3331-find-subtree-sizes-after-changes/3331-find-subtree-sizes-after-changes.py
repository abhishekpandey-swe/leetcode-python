class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        # Original tree.
        children = [[] for _ in range(n)]
        for x in range(1, n):
            children[parent[x]].append(x)

        new_parent = [-1] * n
        stacks = [[] for _ in range(26)]
        preorder = []

        # Iterative DFS: (node, state), state 0 = enter, state 1 = exit.
        st = [(0, 0)]

        while st:
            u, state = st.pop()
            c = ord(s[u]) - ord('a')

            if state == 0:
                # Closest same-character ancestor on the original path.
                new_parent[u] = stacks[c][-1] if stacks[c] else parent[u]

                stacks[c].append(u)
                preorder.append(u)

                # Exit marker.
                st.append((u, 1))

                # Push children in reverse order so they are processed left-to-right.
                for v in reversed(children[u]):
                    st.append((v, 0))
            else:
                # Backtrack: remove u from its character stack.
                stacks[c].pop()

        # Count sizes in reverse original preorder.
        ans = [1] * n
        for u in reversed(preorder):
            if new_parent[u] != -1:
                ans[new_parent[u]] += ans[u]

        return ans