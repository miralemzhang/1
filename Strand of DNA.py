my_string=str(input())
i=0
hubu_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
indexed_string = [(index, char) for index, char in enumerate(my_string)]
h_string = [(index, char) for index, char in enumerate(my_string)]
j=len(my_string)-1
while i<len(my_string):
  if indexed_string[i][1] in hubu_dict:
   h_string[j]=(indexed_string[i][0],hubu_dict[indexed_string[i][1]])
   i=i+1
   j=j-1
      
hubu_string="".join(char for index, char in h_string)
print(hubu_string)
