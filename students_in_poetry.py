#You are adding students to a Poetry class, the size of which is capped at 6. 
#While the length of the students_in_poetry list is less than 6, use .pop() to take a student off the all_students list
#add it to the students_in_poetry list.
#print students_in_poetry 

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

index = 0
while len(students_in_poetry) < 6:
  students_in_poetry += [all_students.pop()]
  index += 1

print(students_in_poetry) 
