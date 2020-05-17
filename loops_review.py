single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares= []

for digits in single_digits:
  print(digits)
  squares.append(digits**2)
  print(squares)
  
cubes = [element**3 for element in single_digits]
print(cubes)
 
