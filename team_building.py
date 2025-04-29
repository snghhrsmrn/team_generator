# team building
import random

"""
1. randomly choose n person
2. remove n chosen person from the list
"""


def team_members(members):
    members_in_team = int(input("Enter number of team members: "))
    while len(members) != 0:
        if len(members) < members_in_team:
            print(members)
            break
        else:
            team = random.sample(members, members_in_team)
            print(team)
        for each_member in team:
            members.remove(each_member)

members = []
no_of_members = int(input("Enter total number of members: "))

for i in range(no_of_members):
    members.append(input(f"Enter member {i+1}: "))

team_members(members)