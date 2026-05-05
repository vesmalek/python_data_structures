current_movies = {
    "Dynasty": "9:00pm",
    "Gotham": "8:30pm",
    "Blacklist": "01:45pm",
    "War Machine": "06:00am",
    "The Rookie": "0830am"
}

print("We're currently showing: ")

print()
for index, key in enumerate(current_movies.keys()):
    print(f"{index + 1}. {key}")
print()
movie = input("Which one do you wanna watch? ")

if current_movies.get(movie):
    print(f"{movie} is showing at {current_movies[movie]}")
else:
    print("Sorry we don't have that!")

