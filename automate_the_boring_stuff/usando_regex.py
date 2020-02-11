# Greedy and NonGreedy
greedy_regex = re.compile('(Ha){3,5}')
mo = greedy_regex.search('HaHaHaHaHa')
mo.group()

non_greedy_regex = re.compile('(Ha){3,5}?')
mo = non_greedy_regex.search('HaHaHaHaHa')
mo.group()

# Abreviate codes and your negations
xmas_regex = re.compile(r'\d+\s\w+')
not_xmas_regex = re.compile(r"\D+\S\W+")
print(xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# makings Class of caracters
vowel_regex = re.compile(r"[aeiouAEIOU]")
vowel_regex.findall('RoboCop eats baby food. BABY FOOD.')

consonant_regex = re.compile(r"[^aeiouAEIOU]")
consonant_regex.findall('RoboCop eats baby food. BABY FOOD.')

# Joker
at_regex = re.compile(r'.at')
at_regex.findall('The cat in the hat sat on the flat mat.')

# replace strings 
names_regex = re.compile(r'Agent (\w)\w*')
names_regex.sub(r'\1***', 'Agent Alice gave the secret documents to Agent Bob.')

# regex with multiple lines
phone_regex = re.compile(r"'(
(\d{3}|\(\d{3}\))? #area code
\d{3} # first three digits
\d{4} % last four digits
)'", re.VERBOSE)

# multiple operators/variables
some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


