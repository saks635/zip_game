import random

print("🎮 Welcome to the Zip Game!")
secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number (1–10): "))
    attempts += 1
    if guess == secret:
        print(f"✅ You Win in {attempts} attempts!")
        break
    elif guess < secret:
        print("⬆️ Too Low! Try again.")
    else:
        print("⬇️ Too High! Try again.")

