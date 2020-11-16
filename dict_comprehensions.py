#create dict
l1=[2,-4,5,6,9,10]
l2={ i:i**2 for i in l1 if i>0 }
print(l2)

#create with the char and its count of occurance
name="abbbcddeeeef ghijkll"
count_ch={ ch:name.count(ch) for ch in set(name)}
print(count_ch)