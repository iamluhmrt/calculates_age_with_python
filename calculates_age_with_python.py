# base year
current_year = int(2023)
# Asks age
year = int(input("What is your year of birth?: "))
# Determine age with calculation
age = (current_year - year)
# Asks (YES or NO)
reply = str(input("Have you already had a birthday this year? "))
# Condition
if reply == "no":
  # Action block
  age -= 1
# Display the message on the screen
print(f' Your age is: {age}')
