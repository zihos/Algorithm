#어른 상어

#N: 공간 크기
#M: 상어 수
#k: 냄새 없어지는 데 걸리는 이동 회수
n, m, k = map(int, input().split())
#공간 입력받기
space = []
for i in range(n):
    space.append(list(map(int, input().split())))

#상어의 방향 저장
shark_dir = list(map(int, input().split()))

#상어의 회전 방향 우선순위
direction_priority = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        direction_priority[i].append(list(map(int, input().split())))

#각 위치마다 상어번호, 위치번호 저장하는 공간
smell = [[[0,0]]* n for _ in range(n)]

#이동 방향: 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#냄새 업데이트
def updateSmell():
    for i in range(n):
        for j in range(n):
            #냄새가 있으면 냄새 시간 -1
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            #상어가 있으면 냄새 시간 k로 설정
            if space[i][j] != 0:
                smell[i][j] = [space[i][j], k]
            

#상어 이동
def moveShark():
    #이동 결과를 위한 공간
    updateSpace = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            #상어가 존재하는 칸
            if space[x][y] != 0:
                direction = shark_dir[space[x][y]-1]
                #냄새가 존재하지 않는 곳이 있는지 확인 check: False->True
                check = False
                for i in range(4):
                    #이동 후 좌표
                    nx = x + dx[direction_priority[space[x][y]-1][direction-1][i]-1]
                    ny = y + dy[direction_priority[space[x][y]-1][direction-1][i]-1]
                    #이동 후 좌표가 범위 내에 존재하는 지 확인
                    if 0 <= nx and nx < n and 0 <= ny and ny <n:
                        #이동 후 위치에 냄새가 있는지 없는지 확인
                        if smell[nx][ny][1] == 0:
                            #상어의 방향 update
                            shark_dir[space[x][y]-1] = direction_priority[space[x][y]-1][direction-1][i]
                            #상어 이동
                            #이동 할 칸에 상어 없는 경우:
                            if updateSpace[nx][ny] == 0:
                                updateSpace[nx][ny] = space[x][y]
                            else:
                                #이동 할 칸에 상어 있는 경우: 작은 번호 상어로 바꿔줌
                                updateSpace[nx][ny] = min(updateSpace[nx][ny],space[x][y] )
                            
                            check = True
                            break
                #이동할 칸 찾은 경우 밑에 부분 건너뜀
                if check:
                    continue
                #다 냄새가 남아있는 경우
                for i in range(4):
                    nx = x + dx[direction_priority[space[x][y]-1][direction-1][i]-1]
                    ny = y + dy[direction_priority[space[x][y]-1][direction-1][i]-1]
                    #이동 후 좌표가 범위 내에 존재하는 지 확인
                    if 0 <= nx and nx < n and 0 <= ny and ny <n:
                        #자기 냄새인지 확인
                        if smell[nx][ny][0] == space[x][y]:
                            #상어 방향 설정
                            shark_dir[space[x][y]-1] = direction_priority[space[x][y]-1][direction-1][i]
                            #상어 이동
                            updateSpace[nx][ny] = space[x][y]
                            break
    return updateSpace

time = 0
while True:
    updateSmell()
    space = moveShark()
    time += 1

    check = True
    for i in range(n):
        for j in range(n):
            if space[i][j] > 1:
                check = False
    
    if check:
        print(time)
        break
    
    if time >= 1000:
        print(-1)
        break




