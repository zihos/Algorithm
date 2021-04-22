#미로찾기

#bfs이용하기 위한 deque import
from collections import deque
#미로 공간 입력받기
n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph=[]

#미로 공간 입력받기
for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            #이동 후 위치 계산
            n_x = x + dx[i]
            n_y = y + dy[i]
            #이동 후 위치가 공간 내부에 벗어난 경우 무시
            if n_x < 0 or n_y < 0 or n_x >= n or n_y >= m:
                continue
            #벽인 경우 무시
            if graph[n_x][n_y] == 0:
                continue
            #이미 방문한 노드가 아닌경우
            if graph[n_x][n_y] == 1:
                graph[n_x][n_y] = graph[x][y] + 1
                queue.append((n_x,n_y))
    
    return graph[n-1][m-1]

print(bfs(0, 0))
#print(graph)

