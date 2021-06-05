def rule_gen(rule):
    A,num = [],rule
    while num!=0:
        A.append(num%3)
        num = num / 3
    while len(A)<=27: A.append(0)
    return A
def evolution_display(width,rule,steps):
    A,S,E = rule_gen(rule),[0 for i in range(width)],[0 for i in range(width)]
    S[width/2] = 1
    print A
    for j in range(steps):
        print S
        for i in range(1,width-1): E[i] = A[9*S[i-1]+3*S[i]+S[i+1]]
        S = [E[i] for i in range(width)]
evolution_display(7,777,250)
