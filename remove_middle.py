#Create a function named remove_middle which has three parameters named lst, start, and end
#The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
#For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed

#Write your function here

def remove_middle(lst, start, end):
  return lst[:start] + lst[end + 1:]

#Uncomment the line below when your function is done

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#The +1 makes it so that it will only print out the one number in between which is 23, rather than also including 16 as well
