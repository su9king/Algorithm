


while True:

    number = int(input())

    if number == 0:
        break
    elif number == 1 :
        print(1)
        continue
    list = [0] * 2 + [1] * ( (number *2) -1 )

    root = (2*number) ** 1/2

    for i in 