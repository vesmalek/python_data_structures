# filter() function - keep items that pass a specific test

prices = [10, 6, 25, 11, 50]

expensive = list(filter(lambda price: price > 10, prices))
print()
print(expensive)