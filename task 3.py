data = [
    {'name': 'Raj', 'score': 85, 'age': 21},
    {'name': 'Anu', 'score': 90, 'age': 20},
    {'name': 'Ravi', 'score': 85, 'age': 22}
]

sorted_data = sorted(data, key=lambda x: (-x['score'], x['age']))

print(sorted_data)
