#크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
    for i in moves:
        for j in range(n):
            if board[j][i-1] != 0:
                if len(basket) == 0:
                    basket.append(board[j][i-1])
                else:
                    last = basket.pop()
                    if last == board[j][i-1]:
                        answer += 1
                    else:
                        basket.append(last)
                        basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
                
    return answer*2