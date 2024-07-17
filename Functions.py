def choose_weapon():
    weapons = ["Axe", "Bow", "Sword"]
    print("What is that weapon that you're holding?")
    for i, weapon in enumerate(weapons, 1):
        print(f"{i}. {weapon}")

    while True:
        try:
            weapon_choice = int(input("\nChoose your weapon by entering the corresponding number: "))
            if 1 <= weapon_choice <= len(weapons):
                chosen_weapon = weapons[weapon_choice - 1]
                print(f"Ah, I see you've chosen the {chosen_weapon}. A wise choice, warrior!")
                break
            else:
                print("That's not a valid choice. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def choose_journey_part1():
    print("There are many creatures in that Cave that you might not have seen in your entire life.")
    print("Are you sure you're going in?")
    choices = ["Yes! Walk in Cautiously", "Yes! Rage In!!", "No. Return back and End Game"]
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            journey_choice = int(input("\nChoose your action by entering the corresponding number: "))
            if 1 <= journey_choice <= len(choices):
                chosen_action = choices[journey_choice - 1]
                if journey_choice == 3:
                    print("You chose to return back and end the game. Goodbye!")
                    return False
                else:
                    print(f"You chose to {chosen_action}. Brace yourself!")
                    return True
            else:
                print("That's not a valid choice. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")