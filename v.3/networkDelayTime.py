import collections
import heapq

#Dijkstra algorithm
class Solution:
    def networkDelayTime(self, times, N, K) :

        q, t, adj = [(0, K)], {}, collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))

        return max(t.values()) if len(t) == N else -1


# Bellman–Ford algorithm
class Solution:
    def networkDelayTime(self, times, N, K):
        distance = [float("inf") for _ in range(N)]
        distance[K-1] = 0
        for _ in range(N-1):
            for u, v, w in times:
                if distance[u-1] + w < distance[v-1]:
                    distance[v-1] = distance[u-1] + w
        return max(distance) if max(distance) < float("inf") else -1



#  Floyd Warshall
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTimeMatrix = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            elapsedTimeMatrix[u - 1][v - 1] = w
        for i in range(N):                      #   Assigning 0 to the diagonal cells
            elapsedTimeMatrix[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    elapsedTimeMatrix[i][j] = min(elapsedTimeMatrix[i][j], elapsedTimeMatrix[i][k] + elapsedTimeMatrix[k][j])
        mx = max(elapsedTimeMatrix[K - 1])
        return mx if mx < float("inf") else -1


if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2

    s = Solution()
    print(s.networkDelayTime(times,N,K))