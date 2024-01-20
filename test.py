import sys
input = sys.stdin.readline

N , L = map(int,input().split())

num_list = list(map(int, input().split()))
temp = [num_list[0]]
min_list = [num_list[0]]

for i in range(1,N):

    if i - L >= 0 : #나가는 값이 있다면
        if temp[0] == num_list[i-L]: #그 값이 최소값 이라면
            del temp[0]

    if temp[0] > num_list[i]:
        temp.clear()
        temp[0] = num_list[i]

    elif len(temp) == 1:
        temp.append(num_list[i])

    elif temp[1] > num_list[i]:
        temp[1] = num_list[i]


    print(temp)
    min_list.append(temp[0])

print(*min_list)