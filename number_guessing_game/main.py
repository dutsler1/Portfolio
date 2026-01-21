import random_generator
valid_difficulties = ['easy', 'medium', 'hard']
attempts = 0

print("Select a difficulty to continue: ")
user_difficulty = input("easy, medium, or hard: ")
print(f"You selected {user_difficulty} difficulty.")

if user_difficulty not in valid_difficulties:
    print("invalid difficulty level")
elif user_difficulty.lower() == 'easy':
    random_number = random_generator.get_random_number('easy')
    print('Choose a number between 1 and 100')
    user_number = int(input())
    while user_number != random_number:
        attempts += 1
        if user_number < random_number:
            print('your guess is to low, try again')
            user_number = int(input())
        elif user_number > random_number:
            print('your guess is to high, try again')
            user_number = int(input())
    print('you guessed the correct number, you win!')
    print(f'It took you {attempts} attempts to guess the correct number.')

elif user_difficulty.lower() == 'medium':
    random_number = random_generator.get_random_number('medium')
    print('Choose a number between 1 and 300')
    user_number = int(input())
elif user_difficulty.lower() == 'hard':
    random_number = random_generator.get_random_number('hard')
    print('Choose a number between 1 and 1000')
    user_number = int(input())