# zip() function in Python

fields = ['username', 'address', 'phone', 'password', 'is_member', 'balance']
values = ['izzy', '5th Ave, New York', '257 788 111 222', '47habr@#$HH', True]

user_response = dict(zip(fields, values))
print()
print(type(user_response))
print()
print(user_response)