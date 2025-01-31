# The goal is to travel from Independence, Missouri to Oregon City, Oregon (2000 miles) by Dec 31st. However, the trail is arduous. 
# Each day costs you food. You can hunt and rest, but you have to get there before winter!

# DETAILS -------------

# Player starts in Independence, Missouri on March 1st with 500lbs of food
# They must make travel 2,000 miles to get to Oregon by December 31st
# At the beginning of the game, user defines names for their wagon leader and four other wagon members
# Each turn, the player is asked what action they choose, where the player can type in the following: travel, rest, hunt, status, help, quit
# Based on what action the player chooses, health, food, and distance traveled is updated
# If a players health drops to zero at the end of a turn, they have a 50% chance of dying 
# If all players are dead, the wagon leader dies, or too much time passes, the game is over
# If the player travels 2,000 miles or more, the game has been won

# They move a random amount between 30 and 60 miles
# Each wagon member has a 20% chance to lower their by 1 point
# Food supply goes down by 3 for each wagon member

# When a player elects to rest:
# They rest a random number of days between 1 and 3
# The food supply goes down by 1 for each wagon member
# Each wagon member has a 50% chance to increase their health by 1

# When a player elects to hunt:
# They hunt for a random amount of days between 1 and 2
# They earn a random amount of food between 20 and 50
# Each wagon member has a 10% chance to lose a health point

# When a player elects to see the status, the following are printed:
# Wagon leader name
# Wagon food supply
# Distance traveled and distance remaining
# For each wagon member:
# Member name
# Member health rating

# When a player elects to get help, the following is printed:
# Travel: Description of travel option
# Hunt: Description of hunt option
# Status: Description of status option
# Quit: Description of quit option

# When a player elects to quit, print the following then quits:
# Wagon Leader
# Distance Traveled
# Food Remaining
# Each wagon member:
# Name
# Health

# To quit a python program, import sys then use sys.quit()

# Create a dictionary with the following keys:
# wagon leader
# food
# miles traveled
# days spent
# wagon members

# Use the following functions to update the dictionary based on input
# Travel
# Hunt
# Status
# Quit
# Help

# TIPS ---------------

# You might want to make a function that takes in the number of days passed and returns the current date! 
# You’ll want to keep track of which days have 31 days
# Each player might need their own dictionary




# BONUS!!!! -------------

# Each wagon member has a chance to get cholera, dysentery or break their arm based on their current health level:
# 5 - 0% 
# 4 - 10%
# 3 - 20%
# 2 - 30%
# 1 - 40%

# When resting, there is a 20% chance the wagon is robbed and loses a random amount of food between 5 and 20

# Make a reflex mini game where player has to earn food
# Ex: print a word and if the user types it in fast enough, they earn 10 food then repeat 5 times