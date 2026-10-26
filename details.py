
# This program collects user details and prints them in a formatted string.

# Prompt the user to input their name
user_name = input("Enter your name:")

# Prompt the user to input their age
user_age = input("Enter your age:")

# Prompt the user to input their house number
house_number = input("Enter your house number:")

# Prompt the user to input their street name
street_name = input("Enter your street name:")

# Print a message that includes the user's name, age, house number, and street name using string formatting
print()
print("This is {}. He is {} years old and lives at house number {} on {}.".format(user_name, user_age, house_number, street_name))
