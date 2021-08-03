groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
groups_dict = dict.fromkeys(groups)

groups_number = int(input())
for i in range(groups_number):
    groups_dict[groups[i]] = int(input())

print(groups_dict)
