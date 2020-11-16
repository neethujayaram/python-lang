for i in range(1,10):
      if i%3 == 0:
         continue
      print(i,end = ' ')

D  = {'Mark':85, 'Tom':65, 'John':37, 'Rob':85 }
for name,age in D.items():
      if age > 65:
          print(name)
          break
else:
     print('No senior citizens')