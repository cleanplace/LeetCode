import heapq
#O(NlogN)/O(N)
#힙정렬 사용 : 힙정렬 방식 자체가... 분할정복기법
class Solution:
    def getSkyline(self, buildings):
        # 정렬을 하고 시작하기에 쉽고 빠르게 접근 가능
        # 규칙
        # 1. 스카이라인이 끊어졌다 -> 다음 L값이 이전 R 값보다 크다
        # 2. 건물의 높이가 달라졌는데, 이전 H보다 건물의 높이가 낮다 -> 낮아진 지점을 기준으로 현재 L값을 R값으로 업데이트

        #python은 기본적으로 minheap이기때문에... -H로 놓고 정렬
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        # res: result, [pos, height]
        # live: heap, [-height, ending position], 스카이라인이 이어졌는지 끊어졌는지 판단

        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, 스카이 라인이 끊어졌다고 판단되는 건물의 L 값을 pop
            # 2, 건물의 스카인라인이 이어지는지 판별
            # 3, 건물의 높이를 검사하여 건물의 시작점, 끝점을 규칙2로 업데이트
            while pos >= live[0][1]: #스카이 라인이 끊어지거나, 건물의 높이가 달라졌다면 pop
                heapq.heappop(live)
            if negH:
                heapq.heappush(live, (negH, R)) #건물의 높이를 검사하여 건물의 시작점, 끝점 업데이트
            if res[-1][1] + live[0][0]: #값이 0이면 동작하지 않음 : 건물의 높이가 낮아진 경우 -> 다음 while문을 돌면서 이전 R 값으로 update
                res += [pos, -live[0][0]],
        return res[1:]

if __name__ == "__main__":
    input =[[2, 9, 10], [3, 7 ,15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    s = Solution()
    print(s.getSkyline(input))
