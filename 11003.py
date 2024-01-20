import sys
from collections import deque
input = sys.stdin.readline

N , L = map(int,input().split())

num_list = list(map(int, input().split()))
min_list = []
temp = deque() #해당 범위내의 최솟값,두번째가 될 최솟값 임시저장소

for i in range(N):

    #나가는 값이 최솟값이라면 그거 빼버리셈 ㅇㅇ
    if i - L >= 0 :
        if temp[0] == num_list[i-L]:
            temp.popleft()

    #들어올 값이 최솟값 임시저장소의 원소보다 작다면 기존 원소 삭제시켜버려 ㄱ
    while len(temp) >= 1 and num_list[i] < temp[-1]:
        temp.pop()

    temp.append(num_list[i])

    min_list.append(temp[0])


print(*min_list)