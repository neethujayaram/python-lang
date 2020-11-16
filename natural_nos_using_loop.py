#while loop
n=5
i=1
sumofnos=0

while i<=n:
    sumofnos+=i
    i+=1

print("Using while loop, sum is ",sumofnos)

#for loop
sumofnos=0
for i in range(1,n+1):
    sumofnos+=i
print("Using for loop, sum is ",sumofnos)

#without any loop
sumofnos=0
sumofnos=sum(range(1,n+1))
print("Using without any loop, sum is ", sumofnos)