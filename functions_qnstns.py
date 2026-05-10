# Q1. Define a function called greet_user that takes a username
#     and prints "Welcome back, ismail!" using the argument passed

def greet_user(username):
    print(f"Welcome back, {username.strip().lower()}!")

print("Question 01:")
greet_user("imran")

# Q2. Define a function called calculate_discount that takes
#     a price and a discount percentage, and RETURNS the final price
#     Test it: calculate_discount(100, 10) should return 90.0

def calculate_discount(price, discount):
    return price * (1 - (discount/100))

final_price = calculate_discount(100, 10)
print()
print("Question 02:")
print(final_price)

# Q3. Define a function called create_product that takes:
#     name, price, and an optional category that defaults to "General"
#     It should RETURN a dictionary with those three keys
#     Call it twice — once with category, once without

def create_product(name, price, category="General"):
    return dict(name=name, price=price, category=category)

print()
print("Question 03:")
print(create_product('Tomato', 12.99, "Groceries"))

print(create_product('Oranges', 5.88))


# Q4. Define a function called validate_login that takes
#     email and password
#     If either is empty, return {"success": False, "error": "All fields required"}
#     Otherwise return {"success": True, "message": "Login successful"}
#     Test it with valid and invalid inputs using keyword arguments

def validate_login(email, password):
    if not email or not password:
        return {"success": False, "error": "All fields required"}
    else:
        return {"success": True, "message": "Login successful"}
    
print()
print("Question 04:")
print(f"{validate_login("john@doe.com", "2783ABX")}")
print(f"{validate_login("john@doe.com", "")}")
print(f"{validate_login("", "2783ABX")}")
print(f"{validate_login("", "")}")

# Q5. Define a function called summarize_order that takes:
#     product_name, quantity, price_per_unit
#     It should return a dict with:
#       - the three inputs
#       - a "total" key calculated inside the function
#     Then call the function and print each key-value pair
#     using a loop (you know how to do this from Phase 2)