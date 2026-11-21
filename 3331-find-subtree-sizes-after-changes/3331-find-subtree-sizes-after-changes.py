class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        import sys
        sys.setrecursionlimit(1_000_000)

        n = len(parent)

        # Original tree.
        children = [[] for _ in range(n)]
        for x in range(1, n):
            children[parent[x]].append(x)

        # Find new parents.
        new_parent = [-1] * n
        stacks = [[] for _ in range(26)]

        def dfs(u: int) -> None:
            c = ord(s[u]) - ord('a')
            new_parent[u] = stacks[c][-1] if stacks[c] else parent[u]

            stacks[c].append(u)
            for v in children[u]:
                dfs(v)
            stacks[c].pop()

        dfs(0)

        # Build the new tree.
        new_children = [[] for _ in range(n)]
        for x in range(1, n):
            new_children[new_parent[x]].append(x)

        # Compute subtree sizes in the new tree.
        ans = [1] * n

        def dfs2(u: int) -> None:
            for v in new_children[u]:
                dfs2(v)
                ans[u] += ans[v]

        dfs2(0)
        return ans
        