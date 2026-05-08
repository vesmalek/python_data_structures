# Q2. You have two separate lists — combine them into a list of dicts
#     usernames = ["ismail", "ali", "fatuma"]
#     emails = ["ismail@mail.com", "ali@mail.com", "fatuma@mail.com"]
#     Expected: [{"username": "ismail", "email": "ismail@mail.com"}, ...]

usernames = ["ismail", "ali", "fatuma"]
emails = ["ismail@mail.com", "ali@mail.com", "fatuma@mail.com"]

user_profiles = [{"username": u, "email": e} for u, e in zip(usernames, emails)]

print()
print(user_profiles)