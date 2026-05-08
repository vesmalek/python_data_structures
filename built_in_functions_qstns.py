# Q1. Use enumerate to print this menu with numbers starting from 1
#     menu = ["Dashboard", "Products", "Orders", "Settings", "Logout"]
#     Expected output:
#     1. Dashboard
#     2. Products ... etc

menu = ["Dashboard", "Products", "Orders", "Settings", "Logout"]

print()
print("Question 01:")
for index, item in enumerate(menu, start=1):
    print(f"{index}. {item}")

# Q2. You have two separate lists — combine them into a list of dicts
#     usernames = ["ismail", "ali", "fatuma"]
#     emails = ["ismail@mail.com", "ali@mail.com", "fatuma@mail.com"]
#     Expected: [{"username": "ismail", "email": "ismail@mail.com"}, ...]

usernames = ["ismail", "ali", "fatuma"]
emails = ["ismail@mail.com", "ali@mail.com", "fatuma@mail.com"]

user_profiles = []

for username, email in dict(zip(usernames, emails)).items():
    user_profile = {}
    user_profile["username"] = username
    user_profile["email"] = email
    user_profiles.append(user_profile)

print()
print("Question 02:")
print(user_profiles)

# Q3. Use map to apply a 10% discount to all prices
#     prices = [100, 250, 80, 500, 30]

# Q4. Use filter to get only users who are both active and verified
#     users = [
#         {"username": "ismail", "is_active": True, "is_verified": True},
#         {"username": "ali", "is_active": True, "is_verified": False},
#         {"username": "fatuma", "is_active": False, "is_verified": True},
#         {"username": "john", "is_active": True, "is_verified": True},
#     ]

# Q5. Combine everything:
#     From the filtered users in Q4, use map to extract just the usernames
#     Then use enumerate starting from 1 to print them like:
#     "1. ismail"
#     "2. john"