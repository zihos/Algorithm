#키패드 누르기
def solution(numbers, hand):
    answer = ''
    keypad = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
    
    left = '*'
    right = '#'
    for n in numbers:
        #1, 3, 7 -> left thumb
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            left = n
        #3, 6, 9 -> right thumb
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            right = n
        #2, 5, 8, 0 -> closest thumb
        else:
            left_now = keypad[left]
            right_now = keypad[right]
            n_position = keypad[n]
            
            left_distance = abs(left_now[0] - n_position[0]) + abs(left_now[1] - n_position[1])
            right_distance = abs(right_now[0] - n_position[0]) + abs(right_now[1] - n_position[1])
            
            if left_distance < right_distance:
                answer += 'L'
                left = n
            elif left_distance > right_distance:
                answer += 'R'
                right = n
            else:
                if hand == "right":
                    answer += 'R'
                    right = n
                else:
                    answer += 'L'
                    left = n
            
    return answer