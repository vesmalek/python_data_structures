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

def calculate_tax(price):
    tax_rate = 0.16
    return price * tax_rate

print()
print("Question 02:")
tax_amount = calculate_tax(50000)
print(f"Tax: ${tax_amount}")

# print(f"Tax rate: {tax_rate}") 

# The compiler throws NameError: name 'tax_rate' is not defined because tax_rate's scope is local, only available in the function where it is defined

# Q3. Create a global variable called visitor_count = 0
#     Define a function called track_visit that increments it by 1
#     using the global keyword
#     Call it 3 times then print visitor_count
#     Then rewrite the same logic WITHOUT using global —
#     pass the count in as a parameter and return the updated value

# Solution 01:
visitor_count = 0

def track_visit():
    global visitor_count
    visitor_count += 1

track_visit()
track_visit()
track_visit()
print()
print(f"Question 3, first alternative:")
print(f"Visitor Count: {visitor_count}")

# Alternative B:

visitor_count = 0

def track_visit2(count):
    return count + 1

track1 = track_visit2(0)
track2 = track_visit2(track1)
track3 = track_visit2(track2)
print()
print(f"Question 3, second alternative:")
print(f"Visitor Count: {track3}")


# Q4. Demonstrate the LEGB rule in one block of code:
#     - Create a global variable x = "global"
#     - Define an outer function with its own x = "enclosing"
#     - Define an inner function inside it with its own x = "local"
#     - Print x from inside inner, from inside outer, and from global level
#     - Expected output:
#       local
#       enclosing
#       global

x = "global"

def outer_function():
    def inner_function():
        x = "local"
        print(x)
    x = "enclosing"
    inner_function()
    print(x)

print()
print("Question 04:")
outer_function()
print(x)

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


# Explanation: The bug is the result of trying to access the value of 'total' in the expression 'total - discount' while total is not yet defined. Therefore, we need to add a line before the expression 'global total' which means anytime in this function I refer to a total I mean the global total

# Solution (The Fix):
total = 500

def apply_discount(discount):
    global total
    total = total - discount
    return total

print()
print("Question 05:")
print(apply_discount(50))