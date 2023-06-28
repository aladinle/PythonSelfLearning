import re

find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
print(find_members)

# solution2:
#find_members.sort()
#print(find_members)