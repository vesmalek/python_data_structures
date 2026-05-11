# Q1. Create a global variable called shop_name with any value.
#     Define a function called display_shop that reads and prints it.
#     Call the function — no modifying, just reading.

shop_name = "Imran Ceramics"

def display_shop():
    print(f"Shop: {shop_name}")

print()
print("Question 01:")
display_shop()

# Q2. Define a function called calculate_tax that creates a local
#     variable called tax_rate = 0.16 and returns a tax amount
#     for a given price: price * tax_rate
#     After calling the function, try to print tax_rate outside it
#     and observe what happens — put the error in a comment

# Q3. Create a global variable called visitor_count = 0
#     Define a function called track_visit that increments it by 1
#     using the global keyword
#     Call it 3 times then print visitor_count
#     Then rewrite the same logic WITHOUT using global —
#     pass the count in as a parameter and return the updated value

# Q4. Demonstrate the LEGB rule in one block of code:
#     - Create a global variable x = "global"
#     - Define an outer function with its own x = "enclosing"
#     - Define an inner function inside it with its own x = "local"
#     - Print x from inside inner, from inside outer, and from global level
#     - Expected output:
#       local
#       enclosing
#       global

# Q5. The function below has a bug — find it, explain it in a comment,
#     and fix it:
#
#     total = 500
#
#     def apply_discount(discount):
#         total = total - discount
#         return total
#
#     print(apply_discount(50))