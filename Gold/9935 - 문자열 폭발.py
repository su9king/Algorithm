# 입력값 처리
string = list(input())
boom = input()
stack = []
boom_len = len(boom)


for i in range(len(string)):

    stack.append(string[i])

    if ''.join(stack[-boom_len:]) == boom:

        del stack[-boom_len:]

if stack:
    result = ''.join(stack)
else:
    result = "FRULA"

print(result)