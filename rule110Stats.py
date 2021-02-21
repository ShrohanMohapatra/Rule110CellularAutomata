from pprint import pprint
def rule110CA(arr):
    CARule = [0,1,1,0,1,1,1,0]
    N = len(arr)
    arrX = [[10 for i in range(N)] for k in range(N)]
    arrX[0] = arr
    for k in range(1,N):
        arrX[k][0] = arrX[k-1][0]
        arrX[k][N-1] = arrX[k-1][N-1]
        for i in range(1,N-1):
            arrX[k][i] = CARule[
                4*arrX[k-1][(i-1)%N]+2*arrX[k-1][i]+arrX[k-1][(i+1)%N]
                ]
    for k in range(1,N-1):
        s,L = 0,0
        for i in range(N-1,N-k-2,-1):
            s,L = s + arrX[k][i], L+1
        print(k, round(s/L,2))
size = 200
array = [0 for i in range(size-1)]
array.append(1)
rule110CA(array)