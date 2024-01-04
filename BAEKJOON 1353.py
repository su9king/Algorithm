S , P = input().split()

S = int(S)
P = int(P)
n = 1

while ( (S/n)**n < P ):

    n += 1

    if n == S:
        break

if n == S:
    print(-1)
elif S > P:
    print(2)
else:
    print(n)