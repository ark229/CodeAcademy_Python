#Create a function called every_three_nums that has one parameter named start
#The function should return a list of every third number between start and 100 (inclusive)

#Write your function here

def every_three_nums(start):
  start = list(range(start, 101, 3))
  return start

#Uncomment the line below when your function is done
print(every_three_nums(91))
