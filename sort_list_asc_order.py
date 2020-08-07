li1=[6,5,8,1]
len_li=len(li1)

#get input wise
li1=list(map(int, input().split()))

for i in range(len_li):
    for j in range(i+1,len_li):
        if li1[i]>li1[j]:
            temp=li1[i]
            li1[i]=li1[j]
            li1[j]=temp

print(li1)