import random

print("🎮 Welcome to Number Guessing Game!")

difficulty = input("Choose difficulty (easy/medium/hard): ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "medium":
    attempts = 7
else:
    attempts = 5

number = random.randint(1, 100)

while attempts > 0:
    guess = int(input(f"Enter your guess (Attempts left: {attempts}): "))
    
    if guess > number:
        print("Too High!")
    elif guess < number:
        print("Too Low!")
    else:
        print("🎉 Correct! You Win!")
        break
    
    attempts -= 1

if attempts == 0:
    print(f"😢 Game Over! The number was {number}")