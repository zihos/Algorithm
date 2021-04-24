#특정 거리의 도시 찾기
from collections import deque
#n=도시 수, m=도로 수, k=최단거리, x=출발도시
n, m, k, x = map(int, input().split())
#그래프 공간 생성
graph = [[] for i in range(n+1)]

#도시 간 도로 입력 받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
           
#최단 거리 체크
distance = [-1]* (n+1)
#시작 노드는 0
distance[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

check = True

for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)