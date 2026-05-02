# LeetCode 684 — Redundant Connection
# Approach: Union-Find (Disjoint Set Union - DSU)
# Idea: Jab bhi do nodes already same set me ho aur edge aaye,
#      wahi edge cycle bana raha hai → wahi answer.

class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)

        # parent[i] = i ka leader (initially har node apna leader)
        parent = list(range(n + 1))

        # rank[i] = tree ki height approx (optimization)
        rank = [1] * (n + 1)

        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compress
            return parent[x]

        # Union two sets
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            # Agar dono ka root same hai → already connected → cycle
            if rootA == rootB:
                return False  # cycle detect

            # Union by rank (chhota tree bada me attach)
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            elif rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            else:
                parent[rootB] = rootA
                rank[rootA] += 1

            return True

        # Har edge process karo
        for u, v in edges:
            if not union(u, v):
                return [u, v]  # yahi redundant edge hai