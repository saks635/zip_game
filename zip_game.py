import random

print("🎮 Welcome to the Zip Game!")
secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1–10): "))
    if guess == secret:
        print("✅ You Win!")
        break
    elif guess < secret:
        print("⬆️ Too Low! Try again.")
    else:
        print("⬇️ Too High! Try again.")
