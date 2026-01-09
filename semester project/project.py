import random

#   ACCOUNT/BANK

accounts = ["Basmaci", "Teague", "Lettuce", "Frank", "Preston"]
balances = [-100000, 2000, 3000, 4000, 5000]

current_account = None
bet = 1 

def bank_menu():
    global current_account
    while True:
        print("\n----- BANK MENU -----")
        print("1. Select Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. List Accounts")
        print("6. Back to Casino")

        option = input("Choose an option: ")

        if option == "1":
            print("\nAccounts:")
            for i, name in enumerate(accounts):
                print(f"{i+1}. {name}")
            choice = input("Select account number: ")
            if choice.isdigit() and 1 <= int(choice) <= len(accounts):
                current_account = int(choice) - 1
                print(f"Logged into: {accounts[current_account]}")
            else:
                print("Invalid selection.")

        elif option == "2":
            if current_account is None:
                print("Select an account first.")
            else:
                print(f"Balance for {accounts[current_account]}: ${balances[current_account]}")

        elif option == "3":
            if current_account is None:
                print("Select an account first.")
            else:
                try:
                    amount = int(input("Deposit amount: "))
                    if amount > 0:
                        balances[current_account] += amount
                        print(f"New balance: ${balances[current_account]}")
                    else:
                        print("Amount must be positive.")
                except:
                    print("Invalid amount.")

        elif option == "4":
            if current_account is None:
                print("Select an account first.")
            else:
                try:
                    amount = int(input("Withdraw amount: "))
                    if 0 <= amount <= balances[current_account]:
                        balances[current_account] -= amount
                        print(f"New balance: ${balances[current_account]}")
                    else:
                        print("Invalid amount or insufficient funds.")
                except:
                    print("Invalid amount.")

        elif option == "5":
            for i in range(len(accounts)):
                print(f"{i+1}. {accounts[i]} - ${balances[i]}")

        elif option == "6":
            return

        else:
            print("Invalid option.")
#       SLOTS
def play_slots():
    global bet
    symbols = ["🍒", "🍋", "🔔", "💎", "7", "🍀"]

    while True:
        print("\n----- SLOTS MENU -----")
        print("1. Spin (uses current bet)")
        print("2. Change Bet Amount")
        print("3. Check Balance")
        print("4. Back to Casino")

        option = input("Choose: ")

        if option == "1":
            if current_account is None:
                print("Select a bank account first.")
                return

            if bet > balances[current_account]:
                print("Not enough balance to cover the bet.")
                continue

            spin = random.choices(symbols, k=3)
            print("\nSpinning...")
            print(f"| {spin[0]} | {spin[1]} | {spin[2]} |")

            if spin[0] == spin[1] == spin[2]:
                winnings = bet * 30
                print(f"🎉 JACKPOT! All three match! You WIN {winnings} coins!")
            elif spin[0] == spin[1] or spin[0] == spin[2] or spin[1] == spin[2]:
                winnings = bet * 2
                print(f"✨ Two symbols match! You win {winnings} coins!")
            else:
                winnings = -bet
                print("No match. You lose your bet.")

            balances[current_account] += winnings
            print(f"New balance for {accounts[current_account]}: ${balances[current_account]}")

        elif option == "2":
            try:
                new_bet = int(input("Enter new bet amount: "))
                if new_bet > 0:
                    bet = new_bet
                    print(f"Bet updated to {bet}")
                else:
                    print("Bet must be positive.")
            except:
                print("Invalid input.")

        elif option == "3":
            if current_account is None:
                print("Select an account first.")
            else:
                print(f"Balance: ${balances[current_account]} (Bet = {bet})")

        elif option == "4":
            return

        else:
            print("Invalid choice.")
#       ROULETTE GAME
def play_roulette():
    global bet
    red_numbers = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
    black_numbers = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}

    while True:
        print("\n----- ROULETTE MENU -----")
        print("1. Bet Red (2x payout)")
        print("2. Bet Black (2x payout)")
        print("3. Bet Even (2x payout)")
        print("4. Bet Odd (2x payout)")
        print("5. Bet Specific Number (0-36) (35x payout)")
        print("6. Change Bet Amount")
        print("7. Check Balance")
        print("8. Back to Casino")

        option = input("Choose: ")

        if option == "8":
            return

        if current_account is None:
            print("Select a bank account first.")
            return

        if option == "6":
            try:
                new_bet = int(input("Enter new bet amount: "))
                if new_bet > 0:
                    bet = new_bet
                    print(f"Bet updated to {bet}")
                else:
                    print("Bet must be positive.")
            except:
                print("Invalid input.")
            continue

        if option == "7":
            print(f"Balance: ${balances[current_account]} (Bet = {bet})")
            continue

        if bet > balances[current_account]:
            print("Not enough balance to cover the bet.")
            continue

        roll = random.randint(0, 36)
        color = "green"
        if roll in red_numbers:
            color = "red"
        elif roll in black_numbers:
            color = "black"

        print(f"\nRoulette rolled: {roll} ({color})")

        if option == "1":  # Red
            if roll in red_numbers:
                winnings = bet * 2
                print(f"You win {winnings} coins on Red!")
                balances[current_account] += winnings
            else:
                print("You lose.")
                balances[current_account] -= bet

        elif option == "2":  # Black
            if roll in black_numbers:
                winnings = bet * 2
                print(f"You win {winnings} coins on Black!")
                balances[current_account] += winnings
            else:
                print("You lose.")
                balances[current_account] -= bet

        elif option == "3":  # Even
            if roll != 0 and roll % 2 == 0:
                winnings = bet * 2
                print(f"You win {winnings} coins on Even!")
                balances[current_account] += winnings
            else:
                print("You lose.")
                balances[current_account] -= bet

        elif option == "4":  # Odd
            if roll % 2 == 1:
                winnings = bet * 2
                print(f"You win {winnings} coins on Odd!")
                balances[current_account] += winnings
            else:
                print("You lose.")
                balances[current_account] -= bet

        elif option == "5":  # Specific number
            try:
                guess = int(input("Pick a number (0–36): "))
            except:
                print("Invalid number.")
                continue

            if guess == roll:
                winnings = bet * 35
                print(f" EXACT MATCH! You win {winnings} coins!")
                balances[current_account] += winnings
            else:
                print("No match. You lose.")
                balances[current_account] -= bet

        else:
            print("Invalid choice.")

        print(f"New balance for {accounts[current_account]}: ${balances[current_account]}")
#       BLACKJACK
def play_blackjack():
    global bet

    def draw_card():
        cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        return random.choice(cards)

    while True:
        print("\n----- BLACKJACK MENU -----")
        print("1. Play Hand (uses current bet)")
        print("2. Change Bet Amount")
        print("3. Check Balance")
        print("4. Back to Casino")

        option = input("Choose: ")

        if option == "4":
            return

        if current_account is None:
            print("Select a bank account first.")
            return

        if option == "2":
            try:
                new_bet = int(input("Enter new bet amount: "))
                if new_bet > 0:
                    bet = new_bet
                    print(f"Bet updated to {bet}")
                else:
                    print("Bet must be positive.")
            except:
                print("Invalid input.")
            continue

        if option == "3":
            print(f"Balance: ${balances[current_account]} (Bet = {bet})")
            continue

        if option == "1":
            if bet > balances[current_account]:
                print("Not enough balance to cover the bet.")
                continue

            player = [draw_card(), draw_card()]
            dealer = [draw_card(), draw_card()]

            print(f"\nYour hand: {player} (Total {sum(player)})")
            print(f"Dealer shows: {dealer[0]}")

            # PLAYER TURN
            while sum(player) < 21:
                print("\n1. Hit")
                print("2. Stand")
                move = input("Choose 1 or 2: ")
                if move == "1":
                    new = draw_card()
                    player.append(new)
                    print(f"You draw {new}. Hand now: {player} (Total {sum(player)})")
                    if sum(player) > 21:
                        print("Bust! You lose.")
                        balances[current_account] -= bet
                        break
                elif move == "2":
                    break
                else:
                    print("Invalid selection. Choose 1 or 2.")

            if sum(player) > 21:
                print(f"New balance: ${balances[current_account]}")
                continue

            # DEALER TURN
            print(f"\nDealer hand: {dealer} (Total {sum(dealer)})")
            while sum(dealer) < 17:
                new = draw_card()
                dealer.append(new)
                print(f"Dealer draws {new}. Dealer total: {sum(dealer)}")

            player_total = sum(player)
            dealer_total = sum(dealer)
            print(f"\nFinal totals -> You: {player_total} Dealer: {dealer_total}")

            # RESULTS
            if dealer_total > 21 or player_total > dealer_total:
                winnings = bet * 2
                print(f" YOU WIN {winnings}!")
                balances[current_account] += winnings
            elif player_total == dealer_total:
                print("Push. Your bet is returned.")
                balances[current_account] += bet
            else:
                print("Dealer wins. You lose your bet.")
                balances[current_account] -= bet

            print(f"New balance for {accounts[current_account]}: ${balances[current_account]}")

        else:
            print("Invalid choice.")
# -CASINO MENU
def main_menu():
    print("Welcome to the Casino program. Select or create an account in Bank menu before playing.")
    while True:
        print("\n====== CARDINAL CASINO ======")
        print("1. Bank")
        print("2. Slots")
        print("3. Roulette")
        print("4. Blackjack")
        print("5. Leave Casino")

        option = input("Choose an option: ")

        if option == "1":
            bank_menu()
        elif option == "2":
            play_slots()
        elif option == "3":
            play_roulette()
        elif option == "4":
            play_blackjack()
        elif option == "5":
            print("Thanks for visiting the casino! Goodbye.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
