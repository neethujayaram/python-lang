#sum of sublist
lista=[[1,2,3], [4,5,6], [7,8,9]]
sum_sublist=[sum(i) for i in lista]
print(sum_sublist)

#cubes of numbers from 2,9
cube_of_nos=[ i*i for i in range(2,10) ]
print(cube_of_nos)

#zip function
l1=[1,2,3]
l2=[10,20,30]
l3=[9,8,7]
total_lists=[sum(i) for i in zip(l1,l2,l3)]
print(total_lists)

#create list without same aliasing
a1=[ [0]*2 for i in range(4) ]
print(a1)
a1[0].append(2)
print(a1)

#if clause in list comprehension
a2=[ n**2 for n in range(10,21) if n%2==0]
print(a2)

#find the palindrome from the list
a3=['uhteen','amma','moon','noon','Aia']
a3=[word for word in a3 if word==word[::-1]]
print(a3)

#multiple if clause
b1='Abc'
b2='XYz'
b3=[ i+j for i in b1 if i.islower() for j in b2 if j.isupper() ]
print(b3)