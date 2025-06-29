#BlackJack Game
import random
from logo import logo

def deal_card():
    '''This function is used
    for return random 
    card.'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def Game_winner(us,cs):
    '''This function is used for declaring the game result.'''
    if us > 21 and cs <= 21:
        print("You went bust! Computer wins! 😢")
    elif us <=21 and cs >21:
        print("Computer went bust! You win! 🎉")
    elif us <=21 and cs <=21:
        if us > cs :
            print("You have the higher score! You win! 🏆")
        elif us < cs :
            print("Computer has the higher score. Computer wins! 🤖")
        else:
            print("It's a tie! Both scored the same. 🤝")
    elif us >21 and cs >21:
        print("Both players went bust! Computer wins by default! 😬")
    else:
        print("Something went wrong! Please restart the game. 🛠️")

def Show_cards_score(user_cards,current_score,computer_cards,computer_score):
    '''This Function is used for showing cards and final score.'''
    print("\n"*100)
    # show user cards and final score
    print(f"Your final hand: {user_cards}, final score: {current_score}")
    # show computer cards and final score
    if current_score <=21:
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    else:
        print(f"Computer's final hand: {computer_cards[0]}, final score: {computer_cards[0]}")

def Game():
    user_cards = []
    computer_cards = []
    computer_score = 0

    # user cards and score
    for i in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
    current_score = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {current_score}")

    # dealer (computer) cards
    while computer_score <17:
        new_card = deal_card()
        computer_cards.append(new_card)
        computer_score = sum(computer_cards)
    print(f"Computer's first card: {computer_cards[0]}")

    # Taking user choice (Hit/Stand)
    while True:
        user_opt = input("Type 'y' for Hit to get another card, type 'n' for Stand to pass: ").lower()
        #Taking acton of user_choice
        if user_opt == 'y':
            new_card = deal_card()
            user_cards.append(new_card)
            current_score = sum(user_cards)
            # current_score = 21
            if current_score < 21:
                print("\n"*100)
                print(f"Your cards: {user_cards}, current score: {current_score}")
                print(f"Computer's first card: {computer_cards[0]}")
            elif current_score == 21:
                # Show cards and score
                Show_cards_score(user_cards,current_score,computer_cards,computer_score)
                # show Game result
                Game_winner(us=current_score,cs=computer_score)
                break
            else:
                # Show cards and score
                Show_cards_score(user_cards,current_score,computer_cards,computer_score)
                # show Game result
                Game_winner(us=current_score,cs=computer_cards[0])
                break

        elif user_opt == 'n':
            # Show cards and score
            Show_cards_score(user_cards,current_score,computer_cards,computer_score)
            # show Game result
            Game_winner(us=current_score,cs=computer_score)
            break
        else:
            print("\n❌ Invalid input! Please try again. 🔁")

# Game()
while True:
    print(logo)
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    #Validation of user_choice
    if user_choice != 'y' and user_choice != 'n':
        print("\n"*100)
        print("\n❌ Invalid input! Please try again. 🔁")
    elif user_choice == 'y':
        print("\n"*100)
        Game()
        # break
    else:
        print("\n"*100)
        print("Maybe next time!")
        break