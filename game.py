from random import randint

pc = randint(0, 10)

print("-=" * 10)
print("GUESS THE NUMBER")
print("-=" * 10)

player = int(input('Choose a number between 0 & 10: '))

while player != pc:
    if player > 10 or player < 0:
        print("Invalid number! Try again.")
    elif player > pc:
        print("Your number is too high, choose another one.")
    elif player < pc:
        print("Your number is too low, choose another one.")

    player = int(input('Choose a number: '))

print(f"CONGRATS!!! The number was {pc}. YOU WON.")
