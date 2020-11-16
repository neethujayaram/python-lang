#Write a loop to iterate over the keys of this dictionary in reverse sorted order
D = { 'apple':210, 'banana':100, 'grapes':90, 'mango':250, 'cherry':225, 'guava':80 }
for fruit in reversed(sorted(D.keys())):
    print(fruit,D[fruit])

#Write a for loop to capitalize each string of this list. Use enumerate().
L = ['this', 'that', 'the', 'hello world']
for i,word in enumerate(L,0):
    L[i]=word.capitalize()
print(L)

#Given a list of integers, write a for loop that multiplies each odd number of the list by 2 and divides each even number by 2. Use if else operator inside the loop.
listA = [15,2,4,3,8,9]
for i in range(len(listA)):
    listA[i]=listA[i]/2 if listA[i]%2==0 else listA[i]*2
print(listA)

#Write a for loop to print the elements of the following list in sorted order without duplicates.
L = [2,4,1,6,7,8,9,7,1,2,6]
print(sorted(set(L)))
