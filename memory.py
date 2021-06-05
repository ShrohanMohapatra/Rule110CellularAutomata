#4007-8206-TX9G9P
def power(x):
    p = 1
    for i in range(x): p = p * 2
    return p
def binary(x):
    C,num = [],x
    while(num!=0):
        C.append(num%2)
        num = num / 2
    for i in range(len(C)/2):
        swap = C[i]
        C[i] = C[len(C)-1-i]
        C[len(C)-1-i] = swap
    return C
def memory_write(I,RW,M):
    H = power(I/2)
    M = (M/(2*H))*2*H + H*RW + M%H if I%2==1 else M
    RW = (M/H)%2 if I%2==0 else RW
    return RW,M
M1 = 0
#M2 = memory_write(7,1,M1)
#print 'Initial memory content ',M1,binary(M1)
#print 'Final memory content ',M2,binary(M2)
#M3 = memory_write(7,0,M2)
#print 'Restored memory content ',M3,binary(M3)
#print 'The reading content ',memory_write(6,1,M3)
#print 'The reading content ',memory_write(8,1,M3)
