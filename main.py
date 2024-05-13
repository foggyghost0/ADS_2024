
"""
Blackjack
"""

import random


def calculate_user_score():
    u1 = random.randint(1, 11)
    u2 = random.randint(1, 11)
    u3 = random.randint(1, 11)
    u4 = random.randint(1, 11)

    int_list = [u1, u2, u3, u4]

    if sum(int_list) < 21 or sum(int_list) == 21:
        return sum(int_list)

    elif sum(int_list) > 21:
            return f"You BUSTED with {new_summ} pal..."
        else:
            return print(new_summ)


def calculate_dealer_score() -> int:
    d1 = random.randint(1, 11)
    d2 = random.randint(1, 11)
    d3 = random.randint(1, 11)
    d4 = random.randint(1, 11)

    dealer_sum = [d1, d2, d3, d4]

    if d1 + d2 == 21:
        print("Dealer Has a Blackjack!")
        return d1 + d2

    elif d1 + d2 >= 17:
        print(f"Dealer drew {d1 + d2} and stands!")
        return d1 + d2

    elif d1 + d2 + d3 > 21:
        print(f"The Dealer BUSTED with {d1 + d2 + d3}")
        return d1 + d2 + d3

    else:
        while True:
            dealer_sum.append(random.randint(1, 11))

            if sum(dealer_sum) > 21:
                print(f"The Dealer BUSTED with {sum(dealer_sum)}")
                return sum(dealer_sum)
            break


print("Hi! Lets play BlackJack ^_*")
print("I'll be the dealer and you are the User")
user_command = None
print('The game will start now. Input "stop" after a round to end the game.')

while True:
    print("OK, The dealer will draw now. Remember - dealer stands on 17 or higher!")



    print(calculate_user_score(a, b, c))
