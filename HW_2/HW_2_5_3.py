import random

suits = ['♠', '♣', '♦', '♥']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [f"{suit}{rank}" for suit in suits for rank in ranks]
random.shuffle(deck)
players = [[], [], [], []]

for i in range(4):
    player_cards = []
    chosen_suit = suits[i]

    suit_cards = [card for card in deck if card.startswith(chosen_suit)]
    selected_suit_cards = random.sample(suit_cards, 4)

    for card in selected_suit_cards:
        deck.remove(card)

    player_cards.extend(selected_suit_cards)

    other_suits = [s for s in suits if s != chosen_suit]

    for suit in other_suits:
        suit_cards = [card for card in deck if card.startswith(suit)]
        selected_card = random.choice(suit_cards)
        player_cards.append(selected_card)
        deck.remove(selected_card)

    players[i] = player_cards

for i, player in enumerate(players):
    print(f"Гравець {i + 1}: {player}")