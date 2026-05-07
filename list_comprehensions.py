# List Comprehensions

# Syntax: list = [result for item in items if condition]

scores = [55, 74, 99, 80, 12, 46, 65, 37, 78, 100]

best_scores = [score for score in scores if score > 75]
print()
print(best_scores)