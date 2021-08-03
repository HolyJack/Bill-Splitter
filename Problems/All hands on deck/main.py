counter = 0
avg = 0
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cards_dict = dict.fromkeys(cards, 2)

for i in range(13):
    cards_dict[cards[i]] += i

for _i in range(6):
    avg += cards_dict[input()]
    counter += 1

print(avg / counter)
