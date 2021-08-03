import random

print("Enter the number of friends joining (including you):")
friends_number = int(input())
if friends_number < 1:
    print("No one is joining for the party")
    exit(0)

print("Enter the name of every friend (including you), each on a new line:")
friends_dict = {}
for _ in range(friends_number):
    friends_dict.update({input(): 0})

print("Enter the total bill value:")
bill = float(input())
split = round(bill / friends_number, 2)
for friend in friends_dict:
    friends_dict[friend] = split

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
answer = input()
if answer == "Yes":
    lucky_name = random.choice(list(friends_dict))
    split = round(bill / (friends_number - 1), 2)
    for friend in friends_dict:
        friends_dict[friend] = split
    friends_dict[lucky_name] = 0
    print("{} is the lucky one!".format(lucky_name))
else:
    print("No one is going to be lucky")

print(friends_dict)
