my_string = str(input())
i=0
indexed_string = [(index, char) for index, char in enumerate(my_string)]
while i<len(my_string):
  if indexed_string[i][1]=='T':
        indexed_string[i]=(indexed_string[i][0],'U')
  i=i+1

modified_string = ''.join(char for index, char in indexed_string)
print(modified_string)
