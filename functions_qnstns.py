# Q1. Define a function called greet_user that takes a username
#     and prints "Welcome back, ismail!" using the argument passed

def greet_user(username):
    print(f"Welcome back, {username.strip().lower()}!")

greet_user("imran")

# Q2. Define a function called calculate_discount that takes
#     a price and a discount percentage, and RETURNS the final price
#     Test it: calculate_discount(100, 10) should return 90.0

def calculate_discount(price, discount):
    return price * (1 - (discount/100))

final_price = calculate_discount(100, 10)
print()
print(final_price)


# Q3. Define a function called create_product that takes:
#     name, price, and an optional category that defaults to "General"
#     It should RETURN a dictionary with those three keys
#     Call it twice — once with category, once without

# Q4. Define a function called validate_login that takes
#     email and password
#     If either is empty, return {"success": False, "error": "All fields required"}
#     Otherwise return {"success": True, "message": "Login successful"}
#     Test it with valid and invalid inputs using keyword arguments

# Q5. Define a function called summarize_order that takes:
#     product_name, quantity, price_per_unit
#     It should return a dict with:
#       - the three inputs
#       - a "total" key calculated inside the function
#     Then call the function and print each key-value pair
#     using a loop (you know how to do this from Phase 2)