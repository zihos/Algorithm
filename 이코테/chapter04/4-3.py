#왕실의 나이트
pos = input()
pos_row = int(pos[1])
pos_col = int(ord(pos[0]))-int(ord('a'))+1

#이동방향 8가지
dir = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1,-2)]

result = 0

for d in dir:
    #우선 이동 후 위치 계산
    next_row = pos_row+ d[0]
    next_col = pos_col+ d[1]
    #이동 후 위치가 공간에 맞는지 검사 후 맞다면 결과값 1증가
    if not (next_row < 1 or next_col < 1 or next_row > 8 or next_col > 8):
        result+=1

print(result)

