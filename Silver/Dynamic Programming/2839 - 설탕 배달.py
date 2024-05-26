data = {3:1,5:1}
input_data = int(input())

for i in range(6,input_data+1):

    if i - 5 in data:

        data[i] = data[i-5] + 1
    elif i - 3 in data:

        data[i] = data[i-3] + 1

    else:
        continue;


if input_data in data:
    print(data[input_data])
else:
    print(-1)




