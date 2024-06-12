N = int(input())
originNumbers = list(map(int,input().split()))

minimizeNumbers = list(set(originNumbers))
#print(minimizeNumbers,originNumbers)
minimizeNumbers.sort(reverse=False)
#print(minimizeNumbers)

dc = {}
index = 0
for i in minimizeNumbers:
     dc[i] = index
     index += 1

for j in originNumbers:
    print(dc[j] , end = " ")
