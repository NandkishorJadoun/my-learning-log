# L1: Unit Tests

# Assignment
def total_xp(level, xp_to_add):
    xp = level * 100
    result = xp + xp_to_add
    return result


# L3: Debugging


# Assignment
def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp
    actual_damage = total_damage - resist
    new_health = health - actual_damage
    return new_health


# L7: Debugging Practice


# Assignment
def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    alert = f"Achievement Unlocked: {ach_name}"
    return after_xp, alert
