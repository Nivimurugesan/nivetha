aa=input().split()
bb=''
for j in aa:
    for yy in range(-1,-len(j)-1,-1):
        b+=j[yy]
    if j!=aa[-1]:
        bb+=" "
print(bb)
