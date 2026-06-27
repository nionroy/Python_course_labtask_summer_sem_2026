from collections import Counter

# Original Dictionary
d = {
    'V': 10,
    'VI': 10,
    'VII': 40,
    'VIII': 20,
    'IX': 70,
    'X': 80,
    'XI': 40,
    'XII': 20
}

# Count frequency of dictionary values
result = Counter(d.values())

print("Original Dictionary:")
print(d)

print("\nFrequency of values:")
print(result)