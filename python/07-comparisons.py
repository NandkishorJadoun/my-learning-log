# L1: Comparison Operators

# Assignment
def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score


# L2: Comparison Operator Evaluations


# Assignment
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height

    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same


# L4: If Statements


# Assignment
def print_status(player_health):
    if player_health <= 0:
        print("dead")
        return

    print("status check complete")


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()
