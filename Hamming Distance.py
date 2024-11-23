my_string1 = str(input())
my_string2 = str(input())
i=0
indexed_string1 = [(index, char) for index, char in enumerate(my_string1)]
indexed_string2 = [(index, char) for index, char in enumerate(my_string2)]
j=0
while i<len(my_string1):
  if indexed_string1[i][1] != indexed_string2[i][1]:
    j=j+1
    i=i+1
  else:
    i=i+1

print(j)
