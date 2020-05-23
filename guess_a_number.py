import random

secret_number = random.randint(1, 20)

for guessTake in range(1, 7):
	print("Chute um número")
	guess = int(input())
	if guess < secret_number:
            print("Muito baixo")
        elif guess > secret_number:
            print("Muito alto")
        else:
            print("Acertou")
