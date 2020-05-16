dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

dog_breed_I_want = 'dalmatian'

for breeds in dog_breeds_available_for_adoption:
  print(breeds)
  if breeds == dog_breed_I_want:
    break
print("They have the dog I want!")
