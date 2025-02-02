from game.characters import cloud, barret  # ✅ No circular import

def open_menu():
    """Allows the player to manage items, equip materia, and adjust their loadout between battles."""
    while True:
        print("\n📜 Menu:")
        print("1. View Stats")
        print("2. Equip Materia")
        print("3. Equip Support Materia")
        print("4. Use Items")
        print("5. Exit Menu")

        choice = input("> ")

        if choice == "1":
            view_stats(cloud)  # ✅ Fixed: Function is now properly defined
        elif choice == "2":
            choose_materia(cloud)
        elif choice == "3":
            choose_support_materia(cloud)
        elif choice == "4":
            cloud.use_item()
        elif choice == "5":
            print("\nExiting Menu...")
            break
        else:
            print("\n⚠️ Invalid choice! Try again.")

def view_stats(player):
    """Displays player's stats and equipped materia."""
    print("\n📊 Character Stats:")
    print(f"Name: {player.name}")
    print(f"Level: {player.level}")
    print(f"HP: {player.hp}/{player.max_hp}")
    print(f"MP: {player.mp}/{player.max_mp}")
    print(f"XP: {player.xp}/{player.xp_to_level}")
    print(f"Attack: {player.attack}")
    print(f"Magic: {player.magic}")
    print(f"Limit Break: {player.limit_break_meter}%")
    print(f"Equipped Materia: {player.equipped_materia.name if player.equipped_materia else 'None'}")
    print(f"Equipped Support Materia: {player.equipped_support_materia.name if player.equipped_support_materia else 'None'}")

def choose_materia(player):
    """Allows the player to change equipped materia."""
    from game.combat import thunder_materia, fire_materia, ice_materia, cure_materia  # ✅ Import inside function

    materia_list = [thunder_materia, fire_materia, ice_materia, cure_materia]

    print("\n🔵 Available Materia:")
    for i, materia in enumerate(materia_list, 1):
        print(f"{i}. {materia.name} ({materia.spell}) [Level {materia.level}]")

    choice = input("\nSelect a materia to equip (1-4) or type 'cancel': ")

    if choice.isdigit() and 1 <= int(choice) <= len(materia_list):
        selected_materia = materia_list[int(choice) - 1]
        player.equip_materia(selected_materia)
    elif choice.lower() == "cancel":
        print("\nNo changes made.")
    else:
        print("\n⚠️ Invalid choice! Try again.")

def choose_support_materia(player):
    """Allows the player to equip support materia like 'All'."""
    from game.combat import all_materia  # ✅ Import inside function

    support_materia_list = [all_materia]

    print("\n🟢 Available Support Materia:")
    for i, materia in enumerate(support_materia_list, 1):
        print(f"{i}. {materia.name}")

    choice = input("\nSelect a support materia to equip (1) or type 'cancel': ")

    if choice == "1":
        player.equip_support_materia(all_materia)
    elif choice.lower() == "cancel":
        print("\nNo changes made.")
    else:
        print("\n⚠️ Invalid choice! Try again.")


