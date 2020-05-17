#Using a list comprehension, create a new list called fahrenheit that converts each element in the celsius list to fahrenheit. 

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp * 9/5 + 32 for temp in celsius]
print(fahrenheit)
