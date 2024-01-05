import random


def main():
    choices = ["rock", "paper", "scissors"]
    player_wins = 0
    print(
        "Welcome to Rock-Paper-Scissors\n"
        "Play by typing in either rock, paper or scissors in each round\n"
        "Let's play!!!\n"
    )

    while True:
        rounds = input("How many rounds you want to play: ")
        if not rounds.isdigit() or rounds == "0":
            print("Type in a number larger than 0!")
        else:
            rounds = int(rounds)
            break

    for round in range(rounds):
        print(f"\n---Round {round+1}---")
        while True:
            player = input("Your turn: ").strip().lower()

            if player not in choices:
                print("Please try again!")
            else:
                # rock: 0 paper: 1 scissors: 2
                bot = choices[random.randint(0, 2)]
                if player == "rock":
                    if bot == "rock":
                        print("Draw!")
                    elif bot == "paper":
                        print("Bot wins!")
                    else:
                        print("You win!")
                        player_wins += 1

                elif player == "paper":
                    if bot == "paper":
                        print("Draw!")
                    elif bot == "scissors":
                        print("Bot wins!")
                    else:
                        print("You win!")
                        player_wins += 1

                elif player == "scissors":
                    if bot == "scissors":
                        print("Draw!")
                    elif bot == "rock":
                        print("Bot wins!")
                    else:
                        print("You win!")
                        player_wins += 1

                break

    print(f"\nWell done! You won {player_wins}/{rounds} rounds!")


if __name__ == "__main__":
    main()
    print("")
