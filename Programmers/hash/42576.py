#완주하지 못한 선수
def solution(participant, completion):
    answer = {}
    
    for p in participant:
        answer[p] = answer.get(p, 0) + 1
    
    for c in completion:
        if answer[c] == 1:
            del answer[c]
        else:
            answer[c] -= 1
    return list(answer)[0]