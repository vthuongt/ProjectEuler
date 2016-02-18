from _ast import Str
def countLetters(n):
    dictionary = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 
                  6:'six', 7:'seven', 8:'eigth' , 9:'nine', 10:'ten', 
                  11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 
                  15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 
                  19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 
                  50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety' 
    }
    if n in dictionary:
        print(dictionary[n],end=' ') 
        return len(dictionary[n])
    elif 20 < n <100:
        rest = n%10
        print(dictionary[n-rest]+" -",end=' ')
        return len(dictionary[n-rest])+countLetters(rest)
    elif 100 <= n < 1000:
        rest = n%100
        if rest == 0:
            print(dictionary[n//100]+ " hundred",end=' ')
            return len(dictionary[n//100]) + 7 # +7+3 for hundred 
        else:
            print(dictionary[n//100]+ " hundred and",end=' ')
            return len(dictionary[n//100]) + 7 + 3 + countLetters(rest) # +7+3 for hundred and 
    else: 
        print('one thousand',end=' ')
        return 11 #n=1000
        

letters = 0
temp = 0
for i in range(1,1001):
    print(str(i)+": ",end='')
    temp = countLetters(i) 
    letters += temp
    print("->"+str(temp)+"\n")
    
print("Number of letters: "+str(letters))

print(countLetters(1))