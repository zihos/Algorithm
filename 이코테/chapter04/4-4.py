#게임 개발

#게임 공간 수 입력받기
n, m = map(int, input().split())
#캐릭터 위치, 방향 입력받기
pos_x, pos_y, _dir = map(int, input().split())
#게임 공간 육지, 바다 구성하기
place = [list(map(int, input().split())) for i in range(n)]
#방문한 곳 표시하기 위한 리스트
visited_place = [[0]* m for _ in range(n)]
#이동방향 - 북, 동, 남, 서
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#왼쪽 회전
def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


#방문 한 곳 count - 시작점이 육지이므로 1부터 시작
count = 1
#한바퀴 돌았는지 체크 위해
turn_time = 0
#시작점은 이미 방분한 것으로 표시
visited_place[pos_x][pos_y] = 1

while True:
    #turn_left
    _dir = turn_left(_dir)
    next_x = pos_x + steps[_dir][0]
    next_y = pos_y + steps[_dir][1]
    #check visited or sea
    #아직 방분 안한 곳이고 육지라면 이동 후 체크
    if visited_place[next_x][next_y] == 0 and place[next_x][next_y] == 0:
        pos_x = next_x
        pos_y = next_y
        visited_place[pos_x][pos_y] = 1
        #이동 회수 증가
        count += 1
        turn_time = 0#회전 횟수 초기화
    else:#못가는 방향인 경우 다시 왼쪽으로 회전하기 위해 회전 횟수 증가
        turn_time += 1
    #그 자리에서 한바퀴 다 돈 경우 
    if turn_time == 4:
        check_x = pos_x - steps[_dir][0]
        check_y = pos_y - steps[_dir][1]
        #뒤로 갈 수 있으면 가기
        if place[check_x][check_y] == 0:
            pos_x = check_x
            pos_y = check_y
        else:#뒤가 바다인 경우 종료
            break
        turn_time = 0 #회전 수 다시 초기화

print(count)
