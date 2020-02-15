# Values, Keys, Items
spam = {'color':'red', 'age':42}

for v in spam.values():
    print(v)

for v in spam.keys():
    print(v)

for v in spam.items():
    print(v)

# Get - if the value don't exists
print(spam.get('color', 0)
print(spam.get('size', 0)

# Set Default value in list
spam.setdefault('size', 'tall')
print(spam)
spam.setdafault('size', 'short')
print(spam)


