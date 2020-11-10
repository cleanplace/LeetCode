import collections,heapq

def findCheapestPrice(n, flights, src, dst, K):
    pq, g = [(0,src,K+1)], collections.defaultdict(dict)

    for s,d,w in flights:
        g[s][d] = w

    while pq:
        cost, s, k = heapq.heappop(pq)
        if s == dst:
            return cost
        if not k: continue
        for d in g[s]:
            heapq.heappush(pq, (cost+g[s][d], d, k-1))
    return -1

if __name__ == "__main__":
    n = 3
    edges = [[0, 1, 100],[1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0

    print(findCheapestPrice(n, edges, src, dst, k))