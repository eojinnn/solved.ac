"""
아이디어
stack사용
시간 복잡도
O(N) stack할 때, 출력할 때 for 문 한번씩
자료구조
stack = []
"""
from collections import deque
n = int(input())
v = int(input())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

print(graph)
    

        