###Write a function called account_generator that takes two inputs, first_name and last_name and 
###concatenates the first three letters of each and then returns the new account name.

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)
print(new_account)
