import sys
priorityQueue = []


def insert(number):

    #여기서의 인덱스들은 트리구조 관점임. 실제 리스트에 값 호출시에는 -1 필요.

    inputIndex = len(priorityQueue) + 1
    priorityQueue.append(number)

    if len(priorityQueue) == 0:
        priorityQueue.append(number)
        return

    while (inputIndex != 1):

        parentNodeIndex = int(inputIndex / 2)

        if priorityQueue[parentNodeIndex - 1] < priorityQueue[inputIndex - 1]: #넣은 값이 부모 노드보다 크다면
            return
        else: #넣은 값이 부모 노드보다 작다면
            priorityQueue[parentNodeIndex - 1] , priorityQueue[inputIndex - 1] = \
                priorityQueue[inputIndex - 1] , priorityQueue[parentNodeIndex - 1] #위치 변환 하고 inputIndex 를 변경.
            inputIndex = parentNodeIndex

def delete():

    if len(priorityQueue) == 0:
        print(0)
        return
    elif len(priorityQueue) == 1:
        print(priorityQueue.pop())
        return

    # 여기서의 인덱스들은 트리구조 관점임. 실제 리스트에 값 호출시에는 -1 필요.
    currentIndex = 1
    print(priorityQueue[0])
    priorityQueue[0] = priorityQueue.pop()

    childNodeIndex = currentIndex * 2

    while (currentIndex*2) <= len(priorityQueue):

        childNodeIndex = currentIndex * 2


        if childNodeIndex + 1 <= len(priorityQueue): #오른쪽 자식 노드도 있다면,

            if priorityQueue[childNodeIndex -1] > priorityQueue[childNodeIndex]: #자식 노드 비교하여 더 작은 자식을 고름.
                minChildNodeIndex = childNodeIndex + 1
            else:
                minChildNodeIndex = childNodeIndex
        else:
            minChildNodeIndex = childNodeIndex

        if priorityQueue[currentIndex - 1] > priorityQueue[minChildNodeIndex - 1]: # 부모노드가 숫자가 더 크다면
            priorityQueue[currentIndex - 1], priorityQueue[minChildNodeIndex -1] = \
                priorityQueue[minChildNodeIndex -1] , priorityQueue[currentIndex -1]

            currentIndex = minChildNodeIndex

        else:
            return


## TEST CASE
chance = int(input())

for i in range(chance):
    number = int(sys.stdin.readline().rstrip())

    if number == 0:
        delete()
    else:
        insert(number)




