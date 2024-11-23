my_string=str(input())
i=0
a=0
c=0
g=0
t=0
indexed_string = [(index, char) for index, char in enumerate(my_string)]
while i<len(my_string):
  if (indexed_string[i][1]=='A'):
      a=a+1
      i=i+1
  elif (indexed_string[i][1]=='C'):
      c=c+1
      i=i+1
  elif (indexed_string[i][1]=='G'):
      g=g+1
      i=i+1
  elif (indexed_string[i][1]=='T'):
      t=t+1
      i=i+1
print(a,c,g,t)
