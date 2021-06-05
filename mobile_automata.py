def rule_gen(translation,movement):
# Translation considers translation encoding, movement considers movement encoding
# Movement encoding refers to the left or right movement of the header
# print(' '.join(map(str,range(1,11)))) -> PRINTING AN ARRAY IN A SINGLE LINE
    T,M,num1,num2 = [],[],translation,movement
    while num1!=0:
        T.append(num1%2)
        num1 = num1 / 2
    while num2!=0:
        M.append(num2%2)
        num2 = num2 / 2
    while len(T)<8: T.append(0)
    while len(M)<8: M.append(0)
    return [T,M]
def evolution_display(width,translation,movement,steps):
    progress = [0 for i in range(width)]
    marker = width/2
    ruleBook = rule_gen(translation,movement)
    check = steps
    while marker>=1 and marker<width-1 and check>=0:
        R = ''
        for i in range(width): R = R + ('  ' if i!=marker else '. ')
        print R
        print(' '.join(map(str,progress)))
        progress[marker] = ruleBook[0][4*progress[marker-1]+2*progress[marker]+progress[marker+1]]
        buffer = ruleBook[1][4*progress[marker-1]+2*progress[marker]+progress[marker+1]]
        marker,check = marker+1 if buffer==0 else marker-1,check-1
evolution_display(5,35,165,250)
