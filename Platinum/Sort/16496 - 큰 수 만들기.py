
A = int( input() )
list = []
list = input().split()

def check(a,b):

    A = a+b
    B = b+a

    if int(A) < int(B):
        return True
    else:
        return False

while True:
    count = 0
    result = ""
    for i in range(len(list)-1):

        if check(list[i],list[i+1]): #합쳤을때 뒤 숫자가 더 크면 위치변경
            list[i],list[i+1] = list[i+1],list[i]
        else:
            count += 1
            result += list[i]

    if count == len(list)-1:
        result += list[len(list)-1]
        break

if int(result) == 0:
    print(0)
else:
    print(result)

