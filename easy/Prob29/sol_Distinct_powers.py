s = set()
for a in range(2,101):
    for b in range(2,101):
        s |= {a**b}
        
print(len(s))

#in short

print(len({a**b for a in range(2,101) for b in range(2,101)}))