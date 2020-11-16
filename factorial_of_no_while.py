n=int(input("enter the number: "))
num=n
fact=1

while num>1:
    fact*=num
    num-=1
print(f'factorial of {n} is {fact}')