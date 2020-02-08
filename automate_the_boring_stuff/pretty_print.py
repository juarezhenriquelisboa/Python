import pprint

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
