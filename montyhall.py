import random

def monty_hall_simulation(trials=10000, doors=3):
    """
    Simulates the Monty Hall problem for a given number of doors.
    Returns win percentages for switching vs staying.
    """
    win_if_switch = 0
    win_if_stay = 0

    for _ in range(trials):
        # Randomly place prize
        prize = random.randint(0, doors - 1)

        # Contestant makes an initial choice
        choice = random.randint(0, doors - 1)

        # Monty opens one door (not chosen and not the prize door)
        possible_doors = [d for d in range(doors) if d != choice and d != prize]
        monty_opens = random.choice(possible_doors)

        # Remaining doors after Monty opens
        remaining_doors = [d for d in range(doors) if d != choice and d != monty_opens]

        # Switching means picking from the remaining doors
        switch_choice = random.choice(remaining_doors)

        # Outcomes
        if switch_choice == prize:
            win_if_switch += 1
        if choice == prize:
            win_if_stay += 1

    return (win_if_switch / trials * 100, win_if_stay / trials * 100)


if __name__ == "__main__":
    trials = 10000

    # Case (a): 3 doors
    switch_win, stay_win = monty_hall_simulation(trials, doors=3)
    print(f" Monty Hall Simulation (3 DOORS) over {trials:,} trials")
    print(f"   → Win % if SWITCH: {switch_win:.2f}%")
    print(f"   → Win % if STAY:   {stay_win:.2f}%\n")

    # Case (b): 4 doors
    switch_win, stay_win = monty_hall_simulation(trials, doors=4)
    print(f" Monty Hall Simulation (4 DOORS) over {trials:,} trials")
    print(f"   → Win % if SWITCH: {switch_win:.2f}%")
    print(f"   → Win % if STAY:   {stay_win:.2f}%")
