N = int(input())
for _ in range(N):
    molla = int(input())

    amounts = [1,2,5,10,20,50,100]
    ans = [0,0,0,0,0,0,0]
    count = 0
    for i in range(len(amounts) - 1,-1,-1):
        if amounts[i] > molla:
            continue
        else:
            prev = molla
            molla -= amounts[i] * (molla // amounts[i])
            ans[i] = abs(molla - prev) // amounts[i]

    print(sum(ans))
    print(' '.join(map(str,ans)))
