N = int( input() )
deque = list(enumerate(map(int, input().split())))

#print(deque)



index = 1

def rotateDeque(count):
    index = len(deque)

    #print("원래 구조 : ", deque)
    if count > 0:
        for i in range(count):
            index -= 1
            deque.append(deque[0])
            del(deque[0])

    else:
        for i in range(-count):
            index += 1
            deque.insert(0, deque.pop())

    #print(count , "번 " + "회전 결과" , deque)
    #print("삭제되어야 할 인덱스 : ",index % len(deque))
    del(deque[index% len(deque)])


answer = []
while len(deque) > 0:

    number = deque[0][0]
    count = deque[0][1]
    print(number+1,end = " ")
    rotateDeque(count)





