N,M,K = map(int,input().split())
board = []
Bboard = []
Wboard = []
for i in range(N):
    board.append(input())

for i in range(N):

    Bbuffer = []
    Wbuffer = []
    WrowWeight = 0
    BrowWeight = 0

    for j in range(M):

        if board[i][j] == "B":

            if (i+j) % 2 == 0:
                Bbuffer.append(0)
                Wbuffer.append(1)
            else:
                Bbuffer.append(1)
                Wbuffer.append(0)

        else:
            if (i+j) % 2 == 0:
                Bbuffer.append(1)
                Wbuffer.append(0)
            else:
                Bbuffer.append(0)
                Wbuffer.append(1)

    Bboard.append(Bbuffer)
    Wboard.append(Wbuffer)

for i in Wboard:
    print(i)
