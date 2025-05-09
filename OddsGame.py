




# Start with $200, then play blackjack or baccarate 
# if we lose a hand, we double the bet size till we win then we restart the bet size

import random

def play_baccarat_martingale():
    balance = 500
    base_bet = 50
    bet = base_bet
    round_num = 1

    print("🎲 Welcome to Baccarat (Banker Bet Only)")
    print("Using Martingale Strategy — Starting Balance: $200")
    input("Press Enter to begin...")

    while balance >= base_bet:
        print(f"\n--- Round {round_num} ---")
        print(f"Current Balance: ${balance:.2f}")
        print(f"Current Bet: ${bet:.2f}")

        input("Press Enter to play the round...")

        roll = random.uniform(0, 100)

        if roll < 45.86:
            # Banker wins (0.95 payout)
            winnings = bet 

            balance += winnings
            print(f"✅ You WIN! +${winnings:.2f}")
            bet = base_bet  # reset
        elif roll < 45.86 + 44.62:
            # Banker loses
            balance -= bet
            print(f"❌ You LOSE! -${bet:.2f}")
            bet *= 2  # double bet
        else:
            # Tie — bet returned
            print(f"➖ TIE! Your bet is returned.")

        round_num += 1

        if balance < bet:
            print(f"\n💀 Not enough funds to continue. Final Balance: ${balance:.2f}")
            break

    print("\n🎮 Game Over!")
    print(f"Total Rounds Played: {round_num - 1}")
    print(f"Final Balance: ${balance:.2f}")

# Run the game
play_baccarat_martingale()


