num1=int(input())
li=[int(xx) for xx in input().split()]
dd=[]
for j in range(0,len(li)):
	ss=li[j:]
	mm=max(ss)
	if li[j]==mm:
		d.append(li[j])  
print(*dd)
print(max(li))
