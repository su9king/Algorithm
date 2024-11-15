num = int(input());
i = 2;

while(num != 1):
    if(num % i == 0):# i로 소인수 분해가 가능하다면
        print(i);
        num = num/i;
    else:
        i += 1;


