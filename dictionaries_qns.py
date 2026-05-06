# Q1. Create a dictionary for a user profile with keys:
#     username, email, age, is_active
#     Use realistic values

user_profile = {
    "username": "izzy",
    "email": "izzy@gmail.com",
    "age": 18,
    "is_active": True
}

# Q2. Access the email using .get() with a fallback of "No email provided"

print()
email = user_profile.get("email", "No email provided")
print(f"{email}")

# Q3. The user just changed their age — update it

user_profile["age"] = 21
print(f"New user age: {user_profile["age"]}")

# Q4. Add a new key "country" with your value
#     Then delete the "is_active" key

user_profile["country"] = "Singapore"
print(f"{user_profile}")

print()
print(f"After Deleting with 'del'")
del user_profile["is_active"]
print(f"{user_profile}")


# Second way to delete if you wanna return a value, but also can handle error better when provided with default return.
print()
print(f"After Deleting with 'pop'")
deleted_item = user_profile.pop("machine", "Not available!")
print(f"{deleted_item}")

# Q5. Loop over the dictionary using .items() and print each
#     key and value in this format → "username: ismail"

print()
for key, value in user_profile.items():
    print(f"{key}: {value}")

# Q6. Create this nested dictionary:
#     An "order" with keys: order_id, total, and a nested "customer"
#     key containing name and email
#     Then access the customer's email by chaining keys