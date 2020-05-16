#We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations of the fictional shop, Gilbert and Ilbert’s Scoop Shop
#We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.

#Go through the sales_data list. Call each inner list location, and print out each location list.

#Within the sales_data loop, go through each location list and add the element to your scoops_sold variable.
#By the end, you should have the sum of every number in the sales_data nested list

#Print out the value of scoops_sold

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for sales in location:
    scoops_sold += sales

print(scoops_sold)
