
N = int( input() )
box = list(map(int, input().split()))
S = int( input() )

for i in range(N):
    max_number_index = box.index( max (box[i:min(S+i+1,N)] ))

    box.insert(i, box[max_number_index])
    del( box[max_number_index+1] )

    S -= max_number_index - i

    if S == 0:
        break

print(*box)