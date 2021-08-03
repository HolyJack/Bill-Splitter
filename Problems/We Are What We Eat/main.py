# the list "meals" is already defined
# your code here
total = 0

for title in meals:
    total += title["kcal"]

print(int(total))
