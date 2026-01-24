# L1: Python Numbers

# Assignment
from ast import Return
from pickle import GET


def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage


# L3: Floor Division

normal_division = 7 / 3  # Result = 2.333
floor_division = 7 // 3  # Result = 2 (Basically Math.floor() of Javascript)


# L7: Scientific Notation

number = 15_000  # equals to 15000 (delimiter)


# Assignment
def max_players_on_server():
    small, medium, large = 1.024e18, 1.024e19, 1.024e20
    return small, medium, large


# L13: Bitwise “&” Operator

# Assignment
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    user_create_guild_permission = user_permissions & can_create_guild
    return user_create_guild_permission


def get_review_bits(user_permissions):
    return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild


# L14: Bitwise “|” Operator


# Assignment
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond


# L15: Damage Meter


# Assignment
def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()

# Ll6: Converting Binary

# Assignment
def binary_string_to_int(num_servers, num_players, num_admins):
    return int(num_servers, 2), int(num_players, 2), int(num_admins, 2)
