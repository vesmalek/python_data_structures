# Q1. Define a function called add_items that accepts any number
#     of item names using *args and prints each one on a new line
#     Test it with 2 calls — one with 3 items, one with 5 items

def add_items(*args):
    for item in args:
        print(item)

print()
print("Question 01:")
add_items('Coconut', 'Sea Weed', 'Cassava')
print()
add_items('Apple', 'Oranges', 'Dragon Fruit', 'Pineapple', 'Kiwi')


# Q2. Define a function called build_profile that accepts **kwargs
#     and returns a dictionary of everything passed in
#     Call it with at least 4 keyword arguments and print the result

def build_profile(**kwargs):
    return kwargs

print()
print("Question 02:")
print(build_profile(username="imran", email="imran@example.com", age=15, interest="Medicine"))

# Q3. You have this function:
#     def create_order(product, quantity, price):
#         return {"product": product, "quantity": quantity, "price": price}
#
#     You have this dict:
#     order_data = {"product": "shirt", "quantity": 3, "price": 29.99}
#
#     Call create_order by unpacking order_data — no hardcoding arguments

order_data = {"product": "shirt", "quantity": 3, "price": 29.99}

def create_order(product, quantity, price):
    return {"product": product, "quantity": quantity, "price": price}

print()
print("Question 03:")
print(create_order(**order_data))

# Q4. Define a function called register_user that takes:
#     a required username, any number of roles via *args,
#     and any extra info via **kwargs
#     It should return a dict with username, roles (as a list), and the extra info merged in
#     Expected output for register_user("ismail", "admin", "editor", country="Tanzania", age=30):
#     {'username': 'ismail', 'roles': ['admin', 'editor'], 'country': 'Tanzania', 'age': 30}

# Q5. Define a function called build_response that takes a status string
#     and **kwargs for any additional data
#     It should return a single dict with status first, then all kwargs merged in
#     Expected output for build_response("success", user="ismail", token="abc123"):
#     {'status': 'success', 'user': 'ismail', 'token': 'abc123'}