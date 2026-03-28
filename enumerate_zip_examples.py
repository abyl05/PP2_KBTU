names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

print("Enumerate:")
for i, name in enumerate(names):
    print(i, name)

print("\nZip:")
for name, score in zip(names, scores):
    print(name, score)

best_name = ""
best_score = 0

for name, score in zip(names, scores):
    if score > best_score:
        best_score = score
        best_name = name

print(f"\nBest student: {best_name} ({best_score})")

paired = list(zip(names, scores))
print("\nPaired list:", paired)

print("\nNames with index > 0:")
for i, name in enumerate(names):
    if i > 0:
        print(name)
