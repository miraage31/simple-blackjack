import random
import art
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_user_choice(prompt):
    """Keep asking for input until user enters 'y' or 'n'"""
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:
            return choice
        print("Invalid input. Please enter 'y' or 'n'.")

def ace_checker(deck, score):
    """Converts an ace to 1 if the score is beyond 21."""
    while 11 in deck and score > 21:
        deck[deck.index(11)] = 1
        score -= 10
    return deck, score

def draw_card(deck, score):
    deck.append(random.choice(cards))
    score = sum(deck)
    return ace_checker(deck, score)

def compare_score(u_score, d_score):
    """Determines who wins the game."""
    if u_score > 21:
        return "Player bust. You lose."
    elif d_score > 21:
        return "Dealer bust. You win!"
    elif u_score == d_score:
        return "Draw!"
    elif u_score > d_score:
        return "You win!"
    else:
        return "You lose!"

def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Start of the loop
while True:
    player_card = []
    dealer_card = []
    
    # Initial deal
    for _ in range(2):
        player_card.append(random.choice(cards))
        dealer_card.append(random.choice(cards))

    player_score = sum(player_card)
    dealer_score = sum(dealer_card)

    # If the player or dealer gets 2 aces
    player_card, player_score = ace_checker(player_card, player_score)
    dealer_card, dealer_score = ace_checker(dealer_card, dealer_score)
    
    print(art.logo)
    print(f"Your cards: {player_card}. Current score: {player_score}")
    print(f"Dealer's first card: {dealer_card[0]}")

    # Check for natural blackjack
    if player_score == 21 or dealer_score == 21:
        if player_score == dealer_score:
            print("Both got a natural blackjack. Draw!")
        elif player_score == 21:
            print("Natural blackjack! You win!")
        
    else:  # Normal game
        # Player's turn
        while player_score < 21:
            if get_user_choice("Type 'y' to hit, 'n' to stand: ") == 'n':
                break
            player_card, player_score = draw_card(player_card, player_score)
            print(f"Your cards: {player_card}. Current score: {player_score}")
            print(f"Dealer's first card: {dealer_card[0]}")

        # Dealer's turn
        if player_score <= 21:
            while dealer_score < 17:
                dealer_card, dealer_score = draw_card(dealer_card, dealer_score)
            
            # Show final hands
            print("\nFinal hands:")
            print(f"Your final hand: {player_card}. Final score: {player_score}")
            print(f"Dealer's final hand: {dealer_card}. Final score: {dealer_score}")
            print(compare_score(player_score, dealer_score))
        else:
            print(compare_score(player_score, dealer_score))

    if get_user_choice("\nPlay another hand? Type 'y' or 'n': ") == 'n':
        break
    clear_screen()

print("Thanks for playing!")