aa1,bb=map(int,input().split())
li=[]
cc=0
kk=[]
for i in range(aa1,bb+1):
        li.append(bin(i)[2::])
for i in range(0,len(li)):
        kk.append(li[i].count("1"))

for i in range(0,len(kk)):
        if kk[i]!=1 and kk[i]!=2:
                for pp in range(2,kk[i]):
                        if kk[i]%pp==0:
                                break
                if pp==kk[i]-1:
                        cc=cc+1
        elif kk[i]==2:
                cc=cc+1
print(cc)
