from random import randint

number = randint(0, 10)

player = int(input('Choose a number between 0 and 10: '))

if player == number:
    print('CONGRATS!! YOU WON!')

else:
    print(f'The CP choice were {number}. Hope you get better luck next time!')
  
