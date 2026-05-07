# Q1. Given this list of numbers, create a new list with only even numbers
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if (number%2)==0]
print()
print(even_numbers)

# Q2. Given this list of products, extract only the names of products
#     that are in stock
#     products = [
#         {"name": "shirt", "price": 29.99, "in_stock": True},
#         {"name": "shoes", "price": 59.99, "in_stock": False},
#         {"name": "hat", "price": 14.99, "in_stock": True},
#         {"name": "belt", "price": 9.99, "in_stock": False},
#     ]

# Q3. You receive raw user input for tags — clean them
#     raw_tags = ["  Python  ", "DJANGO", " api ", "REST", "django"]
#     Strip whitespace, lowercase everything, and remove duplicates
#     Hint: you'll need a list comprehension + one thing from a previous topic

# Q4. Given a list of user dicts, build a new list of strings in this format:
#     "ismail — ismail@mail.com"
#     users = [
#         {"username": "ismail", "email": "ismail@mail.com"},
#         {"username": "ali", "email": "ali@mail.com"},
#         {"username": "fatuma", "email": "fatuma@mail.com"},
#     ]