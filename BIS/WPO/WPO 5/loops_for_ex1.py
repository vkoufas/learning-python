"""
Exercise For Loops - Usernames

Task 1: Create Usernames
 
Write a for loop that iterates over the names list to create a usernames list. 
To create a username for each name, make everything lowercase and replace spaces with underscores. 

Running your for loop over the list: 
    names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
should create the list: 
    usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

HINT: Use the .replace() method to replace the spaces with underscores.

Task 2: Modify usernames with Range

Write a for loop that uses range() to iterate over the positions in usernames to modify the list. 
Like you did in the previous part, change each name to be lowercase and replace spaces with underscores.

"""

# Task 1: create usernames

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    name = name.lower().replace(" ", "_")
    usernames.append(name)

print(usernames)


# Task 2: Modify usernames with Range

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(len(usernames)):
    usernames[i]=usernames[i].lower().replace(" ","_")

print(usernames)

