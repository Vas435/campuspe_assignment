import random

best_score = float('inf')

while True:
    number = random.randint(1, 100)
    attempts = 7
    print("\nI'm thinking of a number between 1 and 100. You have 7 attempts.")
    
    score = None
    for i in range(attempts):
        guess = int(input(f"Attempt {i+1}/{attempts}. Enter guess: "))
        
        if guess == number:
            print(f"Yes, You got it in {i+1} attempts!")
            score = i + 1
            break
        
        diff = abs(number - guess)
        hint = " (Hint: You're within 5!)" if diff <= 5 else ""
        
        if guess < number:
            print(f"Too low!{hint}")
        else:
            print(f"Too high!{hint}")
    
    if score is None:
        print(f"Out of attempts! The number was {number}.")
    else:
        if score < best_score:
            best_score = score
            print(f"New Best Score: {best_score} attempts!")
    
    if input("Play again? (y/n): ").lower() != 'y':
        break
