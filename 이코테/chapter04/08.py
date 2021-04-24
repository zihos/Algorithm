#문자열 재졍렬

#문자열 입력받기
s = input()

alpha = []
string = ''
number = 0

for i in s:
    if 65 <= ord(i) and ord(i)<=90:
        alpha.append(i)
    else:
        num = int(i)
        number += num
    
alpha.sort()
#version1
# for i in alpha:
#     string += i
# print(string, end='')
# print(number)

#version2
if number != 0:
    alpha.append(str(number))

print(''.join(alpha))

