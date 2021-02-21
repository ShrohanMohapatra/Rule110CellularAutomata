from pprint import pprint
def rule110CA(arr,steps):
    CARule = [0,1,1,0,1,1,1,0]
    N = len(arr)
    arrX = [[10 for i in range(N)] for k in range(steps+1)]
    arrX[0] = arr
    s,L = 0,0
    for k in range(1,steps+1):
        for i in range(N):
            arrX[k][i] = CARule[
                4*arrX[k-1][(i-1)%N]+2*arrX[k-1][i]+arrX[k-1][(i+1)%N]
                ]
    for i in range(len(arrX)): pprint(arrX[i])
    if steps<=10:
        print(0)
        return
    for k in range(10,steps+1):
        for i in range(1,k+1):
            s,L = s + arrX[k][i], L+1
    print(s/L)
size = 10
steps = 70
array = [0 for i in range(size-1)]
array.append(1)
rule110CA(array,steps)