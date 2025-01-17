# define the choices array
choices = ["Rock", "Paper", "Scissors"]

def main():
    user_input = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

    # validate user input
    if user_input not in choices:
        raise ValueError("Invalid choice. Please enter Rock, Paper, or Scissors.")
    return True

# run the game
if __name__ == "__main__":
    main()
