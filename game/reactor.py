import time
from game.combat import Character, Enemy, battle
from game.characters import cloud, barret

def reactor_mission():
    """Starts the mission in the Mako Reactor with story choices and battles."""
    print("\n🚆 The train screeches to a halt. The security alarm blares.")
    time.sleep(1)

    print("\n💥 Jessie: 'We're in! Move it, move it!'")
    print("🚀 Barret: 'Alright, SOLDIER boy, let's see what ya got!'")
    time.sleep(2)

    print("\n🤔 How does Cloud respond to Barret?")
    print("1. 'I don’t take orders from you.' (-1 Relationship)")
    print("2. 'Let’s just get this done.' (+1 Relationship)")
    print("3. 'Try to keep up, old man.' (-2 Relationship)")

    choice = input("> ")

    if choice == "1":
        print("\n😡 Barret: 'You better pull your weight, merc!'")
    elif choice == "2":
        print("\n🙂 Barret: 'Hmph. At least you're focused.'")
        print("\n💙 Barret’s opinion of Cloud has improved! (+1 Relationship)")
    elif choice == "3":
        print("\n😠 Barret: 'You got jokes? Just don’t slow us down!'")
    else:
        print("\n🤨 Barret: 'Tch. Whatever. Let's move!'")

    time.sleep(2)

    print("\n⚔️ Shinra Guards rush in to stop you!")
    shinra_guard1 = Enemy("Shinra Guard", hp=30, mp=0, attack=8, magic=0, xp_reward=20)
    shinra_guard2 = Enemy("Shinra Guard", hp=30, mp=0, attack=8, magic=0, xp_reward=20)
    shinra_guard3 = Enemy("Shinra Guard", hp=30, mp=0, attack=8, magic=0, xp_reward=20)

    battle([cloud, barret], [shinra_guard1, shinra_guard2, shinra_guard3], return_after_battle=continue_mission)

def continue_mission():
    """Continues the reactor mission after the initial fight."""
    print("\n🔥 The guards are defeated! Avalanche pushes ahead toward the reactor.")

    print("\n📌 What do you want to do?")
    print("1. Head straight for the reactor core (BOSS FIGHT)")
    print("2. Explore to fight enemies and collect items")

    choice = input("> ")

    if choice == "1":
        print("\n🚀 You push forward, heading straight for the reactor core...")
        reactor_core()
    elif choice == "2":
        print("\n🔍 You explore the reactor, fighting additional Shinra troops.")
        exploration_path()
    else:
        print("\n🤷 Barret: 'No time to waste! Let's move!'")
        reactor_core()

def exploration_path():
    """Allows the player to explore the reactor for extra battles and items."""
    print("\n🔎 You move through the reactor corridors, encountering patrols.")
    time.sleep(1)

    # First exploration battle
    shinra_soldier1 = Enemy("Elite Shinra Soldier", hp=40, mp=0, attack=10, magic=0, xp_reward=25)
    shinra_soldier2 = Enemy("Elite Shinra Soldier", hp=40, mp=0, attack=10, magic=0, xp_reward=25)

    battle([cloud, barret], [shinra_soldier1, shinra_soldier2], return_after_battle=post_exploration)

def post_exploration():
    """Handles post-exploration choices."""
    print("\n🎒 You find a Potion and an Ether on the defeated soldiers.")
    cloud.items["Potion"] += 1
    cloud.items["Ether"] += 1

    print("\n📌 What do you want to do next?")
    print("1. Keep exploring")
    print("2. Head to the reactor core (BOSS FIGHT)")

    choice = input("> ")

    if choice == "1":
        print("\n🔎 You continue deeper, encountering more enemies!")
        shinra_soldier3 = Enemy("Shinra Commander", hp=50, mp=0, attack=12, magic=0, xp_reward=30)
        battle([cloud, barret], [shinra_soldier3], return_after_battle=post_exploration)

        print("\n🎒 You find another Potion!")
        cloud.items["Potion"] += 1

        print("\n🚀 After clearing the area, you head to the reactor core.")
        reactor_core()
    else:
        print("\n🚀 You decide it's time to move on to the reactor core.")
        reactor_core()

def reactor_core():
    """Triggers the final boss fight at the reactor core."""
    print("\n🔥 You reach the reactor core. A large mechanical enemy awaits!")
    time.sleep(2)

    print("\n🤖 Guard Scorpion: 'INTRUDER DETECTED. ELIMINATE.'")
    time.sleep(2)

    guard_scorpion = Enemy("Guard Scorpion", hp=200, mp=0, attack=15, magic=0, xp_reward=100)

    print("\n⚠️ Barret: 'That thing looks like bad news!'")
    print("💡 Tip: The Guard Scorpion is weak to Thunder magic!")
    time.sleep(2)

    battle([cloud, barret], [guard_scorpion], return_after_battle=mission_complete)

def mission_complete():
    """Finishes the reactor mission and transitions the story forward."""
    print("\n💥 BOOM! The Guard Scorpion explodes, sending sparks everywhere.")
    time.sleep(2)

    print("\n🚨 Barret: 'Alright! We did it! Now let’s get outta here!'")
    print("\n⏳ The countdown to escape begins...")
    time.sleep(2)

    print("\n🏃 You rush back through the facility as alarms blare!")
    print("\n🔥 The reactor is about to blow! The mission isn't over yet...")








