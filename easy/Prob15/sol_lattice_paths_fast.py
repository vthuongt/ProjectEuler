mX,mY = 20,20
grid = [[0]*(mX+1) for n in range(0,mY+1)]
for y in range(mY,-1,-1):
    for x in range(mX,-1,-1):
        if x == mX and y == mY:
            grid[y][x] = 1
        elif x == mX:
            grid[y][x] = grid[y+1][x]
        elif y == mY:
            grid[y][x] = grid[y][x+1]
        else:
            grid[y][x] = grid[y+1][x]+ grid[y][x+1]

for i in range(0,len(grid)):
    print(grid[i])
print("Total number of routes: "+str(grid[0][0]))