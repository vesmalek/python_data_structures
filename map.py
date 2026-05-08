# map() function in Python , map, zip, enumerate, filter (map and filter ni older versions za list comprehensions)

prices = [34, 12, 20, 35, 55, 60]

def discount(price):
    return price * 0.5

discounted = list(map(lambda price: price * 0.5, prices))
print()
print(discounted)

discounted2 = list(map(discount, prices))
print()
print(discounted2)

discounted3 = [price * 0.5 for price in prices]
print()
print(discounted3)

emails = ['JOHNDOE@EXAMPLE.CO,', 'STAFF@APPLE.COM']
emails_clean = list(map(str.lower, emails))
print()
print(emails_clean)