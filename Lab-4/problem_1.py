d1 = {
"a": 100,
"b": 200,
"c": 300,

}
#d1 = {'a': 100, 'b': 200, 'c': 300
#d2 = {'a': 300, 'b': 200, 'd':400
d2 = {
"a": 300,
"b": 200,
"d": 400,

}

result = {}
# Add all keys from d1
for key, value in d1.items():
    result[key] = value
# Add keys from d2, adding if exists
for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
print(result) # {'a': 400, 'b': 400, 'c': 300, 'd': 400}
