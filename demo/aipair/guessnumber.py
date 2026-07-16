import random

def get_valid_guess(attempt_num):
    """
    Get and validate user input for a guess.
    Returns a valid integer between 1 and 25, or None if input is invalid.
    """
    while True:
        try:
            user_input = input(f"\nAttempt {attempt_num}/3 - Enter your guess (1-25): ").strip()

            # Check if input is empty
            if not user_input:
                print("❌ Error: Please enter a number, don't leave it blank.")
                continue

            # Check if input contains only digits (and possibly a negative sign)
            if not user_input.lstrip('-').isdigit():
                print("❌ Error: Please enter a valid number (no letters or special characters).")
                continue

            # Convert to integer
            guess = int(user_input)

            # Check if number is in valid range
            if guess < 1 or guess > 25:
                print(f"❌ Error: Number must be between 1 and 25. You entered {guess}.")
                continue

            return guess

        except Exception as e:
            print(f"❌ Error: Something went wrong. Please try again.")

def give_hint(secret_number, guess):
    """
    Provide a helpful hint based on the guess compared to the secret number.
    """
    if guess < secret_number:
        difference = secret_number - guess
        if difference <= 2:
            print("🔥 Very close! Your guess is too low.")
        elif difference <= 5:
            print("🌡️ Getting warmer! Your guess is too low.")
        else:
            print("❄️ Your guess is too low.")
    elif guess > secret_number:
        difference = guess - secret_number
        if difference <= 2:
            print("🔥 Very close! Your guess is too high.")
        elif difference <= 5:
            print("🌡️ Getting warmer! Your guess is too high.")
        else:
            print("❄️ Your guess is too high.")

def play_guessing_game():
    """
    Main function to run the guessing number game.
    """
    print("=" * 50)
    print("🎮 Welcome to the Guessing Number Game! 🎮")
    print("=" * 50)
    print("\n📝 Rules:")
    print("  • I'm thinking of a number between 1 and 25")
    print("  • You have 3 attempts to guess it")
    print("  • I'll give you hints after each guess")
    print("=" * 50)

    # Generate secret number
    secret_number = random.randint(1, 25)
    attempts = 3
    guesses = []

    while attempts > 0:
        # Get valid guess from user
        guess = get_valid_guess(4 - attempts)

        if guess is None:
            continue

        guesses.append(guess)
        attempts -= 1

        # Check if guess is correct
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You got it right! The number was {secret_number}.")
            print(f"   You found it in {4 - attempts} attempt(s)!")
            return True
        else:
            # Give hint
            give_hint(secret_number, guess)

            if attempts > 0:
                print(f"   ⏳ You have {attempts} attempt(s) left.")
            else:
                print(f"\n😢 Game Over! You've used all 3 attempts.")
                print(f"   The secret number was: {secret_number}")
                print(f"   Your guesses were: {guesses}")
                return False

def main():
    """
    Main entry point for the program.
    """
    play_again = True

    while play_again:
        play_guessing_game()

        # Ask if user wants to play again
        while True:
            response = input("\n\n🔄 Do you want to play again? (yes/no): ").strip().lower()

            if response in ['yes', 'y']:
                play_again = True
                print("\n" + "=" * 50)
                break
            elif response in ['no', 'n']:
                play_again = False
                print("\n👋 Thanks for playing! Goodbye!")
                print("=" * 50)
                break
            else:
                print("❌ Error: Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
