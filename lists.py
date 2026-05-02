# Python List

# Creating a List
football_clubs = ["Arsenal", "Manchester City", "Manchester United", "Aston Villa", "Liverpool"]

# Indexing a List
print()
print(football_clubs[0])
print(football_clubs[1])
print(football_clubs[2])
print(football_clubs[3])
print()

for index, club in enumerate(football_clubs):
    print(f"{index + 1}. {club}")

print()

# Negative Indexing
print(football_clubs[-3])