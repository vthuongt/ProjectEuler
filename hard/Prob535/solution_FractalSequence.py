
import math
import cProfile
def f(n):
	return math.floor(n**0.5)

def zoomCount(x,y,mDepth,cDepth,elCounter,currentCircPerDepth):	
	#print("Depth: "+str(cDepth)+ ", x,y: "+str([x,y])+", Counter: "+str(elCounter),end=' ')
	if cDepth == mDepth:
		# dont decent in depth
		#print(str(x)+" "+str(y),end=' ')
		return elCounter,currentCircPerDepth
	else:
		# decent in deeper level
		if not (cDepth in currentCircPerDepth):
			currentCirc = 1
		else:
			currentCirc = currentCircPerDepth[cDepth]
		numCircX,numCircY = f(x),f(y)
		elCounter += numCircX + numCircY
		#print("->"+str(elCounter))
		for i in range(0,numCircX):
			if i == numCircX-1:
				elCounter,currentCircPerDepth = zoomCount(currentCirc, x, mDepth, cDepth+1, elCounter,currentCircPerDepth)
			else:
				elCounter,currentCircPerDepth = zoomCount(currentCirc, currentCirc+1, mDepth, cDepth+1, elCounter,currentCircPerDepth)
			currentCirc+=1
			currentCircPerDepth[cDepth]=currentCirc
		for i in range(0,numCircY):	
			if i == numCircY-1:
				elCounter,currentCircPerDepth =zoomCount(currentCirc, y, mDepth, cDepth+1, elCounter,currentCircPerDepth)
			else:
				elCounter,currentCircPerDepth =zoomCount(currentCirc, currentCirc+1, mDepth, cDepth+1, elCounter,currentCircPerDepth)
			currentCirc+=1
			currentCircPerDepth[cDepth]=currentCirc
		
		return elCounter,currentCircPerDepth

print()
#cProfile.run('zoomCount(1,1,5,1,2,{1:1})')
print(zoomCount(1,1,5,1,2,{1:1}))