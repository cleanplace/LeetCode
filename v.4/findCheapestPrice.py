import collections,heapq

def findCheapestPrice(n, flights, src, dst, K):
    #graph 그리기
    g = collections.defaultdict(dict)
    priority_queue = [(0,src,K+1)]

    for s, d, w in flights:
        g[s][d] = w

    #다익스트라 계산
    while priority_queue:
        cost, s, k = heapq.heappop(priority_queue)
        if s == dst: #도착지가 현재의 위치와 같으면 그때의 cost를 리턴
            return cost
        if not k:
            continue #이동 가능 횟수
        for d in g[s]:
            heapq.heappush(priority_queue, (cost + g[s][d], d, k - 1))
    return -1

if __name__ == "__main__":
    n = 3
    edges = [[0, 1, 100],[1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    print(findCheapestPrice(n, edges, src, dst, k))