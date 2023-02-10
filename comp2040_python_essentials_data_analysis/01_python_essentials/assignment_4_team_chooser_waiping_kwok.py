# COMP2040 Python Essentials With Data Analysis
# Assignment 4: Team Chooser
# Wai Ping KWOK
# Create a random program to form 2 teams from a list of players
# Created on 2023 01 17
# Sample output:
# Players:  ['Pikachu', 'Squirtle', 'Clefairy', 'Jigglypuff',
# 'Vulpix', 'Caterpie', 'Weedle', 'Pidgey', 'Oddish']
# Team names:  ['Grass', 'Fire', 'Water', 'Bug', 'Electric', 'Ice', 'Poison']
# Here are your teams:
# Poison   ['Weedle', 'Jigglypuff', 'Vulpix', 'Oddish', 'Clefairy']
# Ice   ['Pidgey', 'Caterpie', 'Pikachu', 'Squirtle']

# import library
from random import choice

# get players from .txt
players = []
file_players = open('assignment_4_players.txt', 'r')
players = file_players.read().splitlines()
print('Players: ', players)

# get team names from .txt
teamNames = []
file_teams = open('assignment_4_team_names.txt', 'r')
teamNames = file_teams.read().splitlines()
print('Team names: ', teamNames)

teamA = []
teamB = []

# randomly choose players to form two teams
while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    # to break loop if single number of players
    if players == []:
        break

    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

# randomly choose team names
teamA_name = choice(teamNames)
teamNames.remove(teamA_name)

teamB_name = choice(teamNames)
teamNames.remove(teamB_name)

# output the results
print('\nHere are your teams:\n')
print(teamA_name, ' ', teamA)
print(teamB_name, ' ', teamB)
