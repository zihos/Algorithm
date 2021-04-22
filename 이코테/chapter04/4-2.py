#시각
# #enter hour h
h = int(input())

#count 3
count = 0

#count for 3 in time
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)