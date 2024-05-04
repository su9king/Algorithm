num = int(input())
numbers = [0,0];

for i in range(2,num+1):


    previousNumber = numbers[i-1]
    numbers.append(previousNumber+1)

    if i % 2 == 0:

        numbers[i] = ( min(numbers[i], numbers[int(i / 2) ] + 1 ) )

    if i % 3 == 0:

        numbers[i] = ( min(numbers[i], numbers[int(i / 3) ] + 1 ) )





print(numbers[num])