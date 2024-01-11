
N = int( input() )
box = list(map(int, input().split()))
S = int( input() )
count = 0

i = 0
while count < S:

    if i == N:
        break

    if S - count > N - i:

        max_number_index = box.index(max( box[i:] ))

    else:

        max_number_index = box.index(max( box[i : i + (S - count) + 1 ] ) )


    if box[i] != box[max_number_index]:
        buffer = box[max_number_index]
        box[max_number_index] = box[max_number_index-1]
        box[max_number_index-1] = buffer
        count += 1
    else:
        i += 1


print(*box)

