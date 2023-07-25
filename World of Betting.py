import random
import time

print("World of Betting".center(115))
management_wallet = 0
wallet = 0
name = input("\nPlease, Enter your name: ")
age = int(input("\nPlease, Enter your age: "))
if age < 18:
    print("\nSorry, You are too young. ")
    time.sleep(2)
    quit()
while wallet < 50:
    wallet = float(input("\nPlease, Enter the money you would like to start with: "))
    if wallet < 50:
        print("\nSorry, The minimum entry = $50. ")
else:
    print(f"\nWelcome {name} to the world of betting. ")
while True:
    if wallet >= 5:
        pass
    else:
        print("\nPlease, Increase your wallet.")
    action = input("\nWhat would you like to do? (Play, Increase wallet, Wallet, Management wallet, Exit): ").lower()
    if action == "play" and wallet >= 5:
        games = input("\nWhat kind of game would you like? (Guessing, Flip Coin, RPS): ").lower()
        if games == "guessing":
            bet = 0
            while bet < 5 or bet > wallet:
                bet = float(input("\nPlease, Enter your bet: "))
                if bet < 5:
                    print("\nSorry, The minimum bet = $5. ")
                if bet > wallet:
                    print("\nSorry, You don't have enough money.")
            else:
                wallet -= bet
                management_wallet += bet
                print("\nWelcome to the guessing game, Only have 3 attempts. ")
                random_number = random.randint(1, 10)
                number_attempt = 0
                number_guessing = 3
                guess = 0
                while guess != random_number and number_guessing > number_attempt:
                    guess = int(input("\nGuess a number between 1 and 10: "))
                    number_attempt += 1
                    if guess < random_number and number_guessing > number_attempt:
                        print("\nSorry, Guess again too low.")
                    elif guess > random_number and number_guessing > number_attempt:
                        print("\nSorry, Guess again too high.")
                    elif number_guessing == number_attempt and guess != random_number:
                        print(f"\nSorry, You lose. the right number was ({random_number})")
                    else:
                        print(f"\nYeah, You win. guessed the right number ({random_number})")
                        wallet += (bet * 2)
                        management_wallet -= bet
        elif games == "flip coin":
            bet = 0
            while bet < 5 or bet > wallet:
                bet = float(input("\nPlease, Enter your bet: "))
                if bet < 5:
                    print("\nSorry, The minimum bet = $5. ")
                if bet > wallet:
                    print("\nSorry, You don't have enough money.")
            else:
                wallet -= bet
                management_wallet += bet
                print("\nWelcome to the flip coin game, Best of 3. ")
                word = ["head", "tail"]
                user_score = 0
                com_score = 0
                while user_score < 2 and com_score < 2:
                    random_word = random.choice(word)
                    guess_word = input("\nGuess the side of coin (Head or Tail): ").lower()
                    if guess_word != random_word:
                        com_score += 1
                        print(f"\nYou lose this round. the right side was ({random_word})")
                    if guess_word == random_word:
                        user_score += 1
                        print(f"\nYou win this round. guessed the right side ({random_word})")
                    print(f"\nYour Score: {user_score} | Computer Score: {com_score} ")
                    if com_score == 2:
                        print("\nSorry, You lose the game.")
                    if user_score == 2:
                        print("\nYeah, You win the game.")
                        wallet += (bet * 2)
                        management_wallet -= bet
        elif games == "rps":
            bet = 0
            while bet < 5 or bet > wallet:
                bet = float(input("\nPlease, Enter your bet: "))
                if bet < 5:
                    print("\nSorry, The minimum bet = $5. ")
                if bet > wallet:
                    print("\nSorry, You don't have enough money.")
            else:
                wallet -= bet
                management_wallet += bet
                print("\nWelcome to the rock, paper, scissor game, Best of 3. ")
                words = ["rock", "paper", "scissor"]
                player_score = 0
                computer_score = 0
                while player_score < 2 and computer_score < 2:
                    random_rps = random.choice(words)
                    choose_word = input("\nChoose between (Rock or Paper or Scissor): ").lower()
                    if choose_word == random_rps:
                        print(f"\nDraw. the computer chose ({random_rps})")
                    elif choose_word == "rock" and random_rps == "scissor":
                        player_score += 1
                        print(f"\nYou win this round. the computer chose ({random_rps})")
                    elif choose_word == "rock" and random_rps == "paper":
                        computer_score += 1
                        print(f"\nYou lose this round. the computer chose ({random_rps})")
                    elif choose_word == "scissor" and random_rps == "rock":
                        computer_score += 1
                        print(f"\nYou lose this round. the computer chose ({random_rps})")
                    elif choose_word == "scissor" and random_rps == "paper":
                        player_score += 1
                        print(f"\nYou win this round. the computer chose ({random_rps})")
                    elif choose_word == "paper" and random_rps == "rock":
                        player_score += 1
                        print(f"\nYou win this round. the computer chose ({random_rps})")
                    elif choose_word == "paper" and random_rps == "scissor":
                        computer_score += 1
                        print(f"\nYou lose this round. the computer chose ({random_rps})")
                    print(f"\nYour Score: {player_score} | Computer Score: {computer_score} ")
                    if computer_score == 2:
                        print("\nSorry, You lose the game.")
                    if player_score == 2:
                        print("\nYeah, You win the game.")
                        wallet += (bet * 2)
                        management_wallet -= bet
    elif action == "increase wallet":
        money = float(input("\nPlease, Enter the money you would like to add to your wallet: "))
        wallet += money
    elif action == "wallet":
        print(f"\nYou have ${format(wallet, ',')} in your wallet.")
    elif action == "management wallet":
        print(f"\nThere are ${format(management_wallet, ',')} in management wallet. ")
    elif action == "exit":
        break