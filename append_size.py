#Create a function called append_size that has one parameter named lst. 
#The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

#Write your function here

def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done

print(append_size([23, 42, 108]))
