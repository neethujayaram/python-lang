#sample program 1
name = input("enter name: ")

while not name.istitle():
    print('wrong name')
    name=input("enter name: ")

print(name)

#sample program 2
n=1
while n<=20:
    print("Hello " * n)
    n+=2
print("Bye")

#sample program 3
#infinite loop
# while True:s

n=2345
sum=0
while n>0:
      rem = n%10
      sum+=rem
      n//=10
print(sum)