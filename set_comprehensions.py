

#Write a list comprehension to create a list that contains root of only positive numbers in this list
L = [81, -9, 4, 16, -25, 64]
root_l=[ n ** .5 for n in L if n > 0]
print(root_l)

#Get the not alpha and numeric values
text="Hello !!! How are you ??? Neethu here ..."
not_alpnum={ ch for ch in text if not ch.isalnum() }
print(not_alpnum)
li_not_alpnum=[ ch for ch in text if not ch.isalnum() ]
print(li_not_alpnum)


