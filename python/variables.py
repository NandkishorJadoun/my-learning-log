# L1: Variables

# Assignment
from sys import platform

player_health = 1000
print(player_health)

# L2: Variables Vary

# Assignment
player_health -= 100
print(player_health)
player_health -= 100
print(player_health)
player_health -= 100
print(player_health)
player_health -= 100
print(player_health)

# L3: Math

# Assignment
player_health = 1000
armor_multiplier = 2
armored_health = player_health * armor_multiplier
print(armored_health)


# L5: Comments

"""
    use docstrings for multiline comments
"""

# L8: Basic Variable Types

"""
    1. strings
    2. numbers
    3. booleans
    4. None (basically null of js)
"""

# L9: F-Strings in Python (we can create strings that contain dynamic values with the f-string syntax)

# Assignment
name = "Yarl"
age = 37
race = "dwarf"

print(f"{name} is a {race} who is {age} years old.")

# L10: NoneType Variables

# Assignment
enemy = None
print(enemy is None)
print(type(enemy))

# L13: Math With Strings

# Assignment
sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

print(sentence_start + player1_health + sentence_end)
print(f"{sentence_start}{player2_health}{sentence_end}")
