def decimals(denominator,output=True):
    """Returns in first argument True if cyclic decimals, otherwise False and in second argument the length of the decimals 
    
    
    Keyword arguments:
    denominator -- the number which 1 is to be divided with
    output -- boolena parameter which defines wether the decimals should be printed (default True)
    """
    dec = ""
    remainder = [1]
    tempRemainder = -1
    while True:
        tempRemainder  = remainder[-1]*10
        dec += str(tempRemainder//denominator)
        remainder +=[tempRemainder%denominator]
        if (remainder[-1] in remainder[:-1]) or (remainder[-1] == 0):
            break
    if output:
        print("1/"+str(denominator)+" = 0.",end='')
        if remainder[-1] == 0:
            print(dec)
        else:
            index = remainder.index(remainder[-1])
            print(str(dec[:index])+"("+str(dec[index:]+")"))
            
    return (remainder[-1] != 0, len(dec))
     
        

cycleLenght = {}
for n in range(1,1000):
    temp = decimals(n)
    if temp[0]:
        cycleLenght[n]=temp[1]
        
maxKey = max(cycleLenght.keys(), key = lambda x: cycleLenght[x])
print("Lenght of longest cylce {} with denominator {}".format(cycleLenght[maxKey],maxKey))


    