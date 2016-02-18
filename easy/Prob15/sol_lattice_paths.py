#too slow on large field
def decent_helper(x,y,mX,mY,counter):
    if x == mX and y == mY:
        return counter+1
    else:
        if x < mX:
            counter = decent_helper(x+1, y, mX, mY, counter)
        if y < mY:
            counter = decent_helper(x, y+1, mX, mY, counter)
        
    return counter
  
def decent(mX,mY):
    return decent_helper(0,0,mX,mY,0)



print(decent(3, 3))