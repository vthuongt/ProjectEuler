from datetime import *
print("Today is: "+str(date.today()))

startDate = date(1901,1,1)
tempDate = startDate
endDate = date(2000,12,31)
SundaysCounter = 0
d = timedelta(days=1)
while tempDate <= endDate:
    
    if tempDate.weekday() == 6 and tempDate.day == 1:
        SundaysCounter +=1
    tempDate += d

print(SundaysCounter)

# better solution
def main():
    sundayCount = 0
    
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.date(year,month,1).weekday() == 6:
                sundayCount += 1

    return sundayCount