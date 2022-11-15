import sys, heapq
#heapq 이진트리 기반의 최소 힙 자료 구조 제공 (큐 우선순위라고 불림) -> 원소들이 항상 정렬된 상태로 추가되고 삭제된다. 

# 힙 큐 관련해서 알아두면 좋을 듯 
N=int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for i in range(N)]
heapq.heapify(cards)

cnt = 0
while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, tmp) 
    cnt += tmp

print(cnt)
