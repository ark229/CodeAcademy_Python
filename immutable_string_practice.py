###The most recent hire at Copeland’s Corporate Company is a fellow named Rob Daily. Unfortunately, 
###Human Resources seem to have made a bit of a typo and sent over the wrong first_name.

###Strings are immutable, so we can’t change an individual character. Okay, that’s no problem we can still fix this!
##Concatenate the string "R" with a slice of first_name that includes everything but the first character 
###and save it to a new string fixed_first_name.

first_name = "Bob"
last_name = "Daily"


fixed_first_name = "R" + first_name[1:]

print(first_name)
print(fixed_first_name)
