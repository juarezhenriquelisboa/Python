# Append and Insert
spam = ['cat','dog','bat']
pam.append('moose')
spam.insert(1, 'chicken')
print(spam)

# Search with Index
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')

# Reversing lists
spam = [2, 5, 3, 1]
spam.sort(reverse=True)

# List items to var
spam = ['cat','dog','bat']
animal1, animal2, animal3 = spam

# References
spam [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
print(spam, cheese) # the same list in both var

# Copy a list
import copy
spam [0, 1, 2, 3, 4, 5]
cheese = copy.copy(spam)
cheese[1] = 'Hello'
print(spam, cheese) # not the same list

''' Use deepcopy to lists in lists or dicts '''




