#럭키 스트레이트
n = input()
half = int(len(n)/2)
num = int(n)

left=0
right=0


for i in range(len(n)):
    mol = num%10
    num = int(num/10)
    if i < half:
        right += mol
    else:
        left += mol

if(left == right):
    print("LUCKY")
else:
    print("READY")

