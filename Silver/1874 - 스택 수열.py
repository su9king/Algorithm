count = int(input())
stack,sequence,result = [] , [] , []
i = 1

for n in range(count):
    inputNum = int(input())

    while i <= inputNum:
        stack.append(i)
        i += 1
        result.append("+")

    if stack[-1] == inputNum:
        sequence.append(stack.pop())
        result.append("-")

    else:
        print("NO")
        break

if len(sequence) == count:
    for j in result:
        print(j)








