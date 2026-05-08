users = {'ismail': 'ismail@mail.com', 'ali': 'ali@mail.com', 'fatuma': 'fatuma@mail.com'}

user_profiles = []
for username, email in users.items():
    user_profile = {}
    user_profile["username"] = username
    user_profile["email"] = email
    user_profiles.append(user_profile)

print()
print(user_profiles)

