# the list "walks" is already defined
# your code here
total = 0
counter = 0

for day in walks:
    total += day["distance"]
    counter += 1

print(int(total / counter))
