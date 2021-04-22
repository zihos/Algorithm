#상하좌우
#공간크기
n = int(input())
#출발위치
x, y = 1, 1
#이동계획
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

next_x, next_y = 0, 0

for plan in plans:
    for i in range(len(move_types)):
        #계획이랑 맞는 move 찾으면 일단 이동한 후 좌표 구하기
        if plan == move_types[i]:
            next_x = x + dx[i]            
            next_y = y + dy[i]

        #이동한 좌표가 공간에 맞는지 체크해서 벗어나면 무시
        if next_x < 1 or next_y < 1 or next_x > n or next_y > n:
            continue
        #이동한 좌표가 공간에 맞으면 위치 업데이트
        x, y = next_x, next_y


print(x, y)
            
