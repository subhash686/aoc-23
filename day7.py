import os
from functools import cmp_to_key

HAND_STRENGTH = {5: 7, 41: 6, 32: 5, 311: 4, 221: 3, 2111: 2, 11111: 1}

CARDS = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
CARDS_2 = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}


def winning_bid(part):
    path = os.getcwd()
    file_path = os.path.join(path, 'day7.txt')
    filel = open(file_path, 'r')
    Lines = filel.readlines()

    hands = []
    for line in Lines:
        hands.append(line.split())

    if part == 1:
        sorted_hands = sorted(hands, key=cmp_to_key(compare))
    else:
        sorted_hands = sorted(hands, key=cmp_to_key(compare2))
    
    product = 0
    for x in range(1, len(sorted_hands)+1):
        product += (x * int(sorted_hands[x-1][1]))
    print(product)


def compare(handb1, handb2):
    hand1 = handb1[0]
    hand2 = handb2[0]
    hand1_str = HAND_STRENGTH.get(int(get_hand(hand1))) 
    hand2_str = HAND_STRENGTH.get(int(get_hand(hand2)))

    # print(hand1_str, hand2_str)
    if hand1_str == hand2_str:
        x = 0
        while x < 5:
            card1_str = int(CARDS.get(hand1[x], hand1[x]))
            card2_str = int(CARDS.get(hand2[x], hand2[x]))

            if card1_str != card2_str:
                break
            x += 1
        return card1_str - card2_str
    return hand1_str - hand2_str

def compare2(handb1, handb2):
    hand1 = handb1[0]
    hand2 = handb2[0]
    hand1_str = HAND_STRENGTH.get(int(get_hand_2(hand1))) 
    hand2_str = HAND_STRENGTH.get(int(get_hand_2(hand2)))

    # print(hand1_str, hand2_str)
    if hand1_str == hand2_str:
        x = 0
        while x < 5:
            card1_str = int(CARDS_2.get(hand1[x], hand1[x]))
            card2_str = int(CARDS_2.get(hand2[x], hand2[x]))

            if card1_str != card2_str:
                break
            x += 1
        return card1_str - card2_str
    return hand1_str - hand2_str


def get_hand(hand):
    caount_map = {}

    for h in range(0, 5):
        card = CARDS.get(hand[h], hand[h])
        caount_map[card] = caount_map.get(card, 0) + 1 
    
    strg=""
    for value in caount_map.values():
        strg += str(value) if value != 0 else ""

    strg = "".join(sorted(strg, reverse=True))
    return strg


def get_hand_2(hand):
    caount_map = {}
    for h in range(0, 5):
        card = CARDS_2.get(hand[h], hand[h])
        caount_map[card] = caount_map.get(card, 0) + 1

    strg = ""
    for key, value in caount_map.items():
        if key != 1:
            strg += str(value) if value != 0 else ""

    strg = "".join(sorted(strg, reverse=True))

    if len(strg) > 0:
        wild = int(strg[0]) + caount_map.get(1,0)
        strg = str(wild) + strg[1:]
    else:
        strg = caount_map.get(1,0)
    return strg

if __name__ == "__main__":
    winning_bid(1)
    winning_bid(2)
