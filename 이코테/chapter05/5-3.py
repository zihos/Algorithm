#음료수 얼려먹기

#공간 크기 입력받기
n, m = map(int, input().split())
#공간
graph = []
#공간 2차원 리스트로 입력받기
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x,y):
    #범위 밖으로 벗어나면 False
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    #방문 안한 노드
    if graph[x][y] == 0:
        graph[x][y] = 1 #방문 처리
        #상하좌우로 dfs재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    #아무것도 방문할 수 없는 경우 False return - 탐색 종료
    return False

count_icecream = 0
#graph를 돌면서 탐색
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count_icecream += 1

print(count_icecream)
        
