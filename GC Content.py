mmp=1
while mmp==1:
 m=str(input())
 if (m=="stop"):
   print(m0)
   print(100*k0)
 else:
    m0=""
    i=0
    k0=0
    j=0
    my_string1=str(input())
    indexed_string1 = [(index, char) for index, char in enumerate(my_string1)]
    while i<len(my_string1):
     if (indexed_string1[i][1]=='C' or indexed_string1[i][1]=='G'):
      j=j+1
     i=i+1
    k=float(j/len(my_string1))
    if k>k0:
      k0=k
      m0=m
  
