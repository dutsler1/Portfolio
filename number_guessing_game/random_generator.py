import random
random_number_easy = random.randint(1, 100)
random_number_medium = random.randint(1, 300)
random_number_hard = random.randint(1, 1000)

def get_random_number(difficulty):
    if difficulty.lower() == 'easy':
        return random_number_easy
    elif difficulty.lower() == 'medium':
        return random_number_medium
    elif difficulty.lower() == 'hard':
        return random_number_hard
    else:
        print("invalid difficulty level")
