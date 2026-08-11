import random

number = random.randint(1, 1000)
attempts = 0

print("🎯 Я загадал число от 1 до 1000s.")
print("Попробуй угадать!")

while True:
    guess = int(input("Твоё число: "))
    attempts += 1

    if guess < number:
        print("Моё число больше!")
    elif guess > number:
        print("Моё число меньше!")
    else:
        print(f"🎉 Правильно! Ты угадал за {attempts} попыток.")
        break