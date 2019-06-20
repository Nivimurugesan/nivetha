Aa=int(input())
Bb=list(map(int,input().split()))
Cc=[]
Dd1=1
for i in Bb:
  if i not in Cc:
    Cc.append(i)
for i in range(len(Cc)-1):
  if (Cc[i]<Cc[i+1]):
    Dd1+=1
print(Dd1)
