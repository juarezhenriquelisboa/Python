# Raw strings
print(r"Bla Bla\'s bla")

# Print multiple lines
print("""Lorem ipsum,

bla bla bla.

Att.""")

# isX
'''
isalpha() abc...
isalnum() abc123
isdecimal() 0123
isspace() \n\t
istitle() Title
'''

# if start or end
'Hello world'.startswith('Hello')
'Hello world'.endswith('world')

# Join
lista = ['My', 'name', 'is', 'Juarez']
','.join(lista)
' '.join(lista)
'ABC'.join(lista)
lista = ' '.join(lista)
lista.split()
lista.split('m')

# Justifying
'Hello'.rjust(20, '*')
'Hello'.ljust(20, '-')
'Hello'.center(20)
'Hello'.center(20, '=')

# Strip
spam = '    Hello    '
spam.strip()
spam.lstrip()
spam.rstrip()
spam = "SpamSpamBlaBlaSpamSpam"
spam.strip('ampS')



