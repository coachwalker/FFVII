from game.relationships import relationship_manager

def start_game():
    print("\nBarret glares at you. 'Cloud! You ready for this?'")

    print("\n1. 'Let's get this over with.' (Barret +1)")
    print("2. 'I don't care. Just pay me.' (Barret -1)")
    print("3. 'I used to be SOLDIER... this feels wrong.' (Jessie +1)")

    choice = input("> ")

    if choice == "1":
        print("\nBarret smirks. 'That's the attitude we need!'")
        relationship_manager.adjust_relationship("Barret", 1)
    elif choice == "2":
        print("\nBarret scoffs. 'Hmph. Just don't slow us down.'")
        relationship_manager.adjust_relationship("Barret", -1)
    elif choice == "3":
        print("\nJessie gives you a curious look. 'SOLDIER, huh? That explains a lot.'")
        relationship_manager.adjust_relationship("Jessie", 1)
    else:
        print("\nBarret raises an eyebrow. 'You listening? Pick one!'")
        return start_game()

