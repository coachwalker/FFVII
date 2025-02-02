import random
import time
from game.core import Character, Materia  
from game.characters import cloud, barret  
from game.menu import open_menu  

class Enemy(Character):
    """Represents an enemy with AI logic."""
    def __init__(self, name, hp, mp, attack, magic, xp_reward):
        super().__init__(name, hp, mp, attack, magic)  # ✅ Fixed order of parameters
        self.xp_reward = xp_reward

    def enemy_attack(self, player):
        """Enemy attacks a random player in the party."""
        damage = random.randint(self.attack - 3, self.attack + 3)
        player.hp -= damage
        player.limit_break_meter += 10  # ✅ Increases Limit Break meter when hit
        print(f"\n⚔️ {self.name} attacks {player.name} for {damage} damage!")
        display_damage_animation()

    def is_alive(self):
        """Checks if the enemy is still alive."""
        return self.hp > 0

def battle(players, enemies, return_after_battle=None):
    """Handles turn-based combat with full HP display, Limit Breaks, and enemy targeting."""
    
    print("\n⚔️ Enemies appear! ⚔️")
    for enemy in enemies:
        print(f" - {enemy.name} (HP: {enemy.hp}/{enemy.max_hp})")

    while any(player.hp > 0 for player in players) and any(enemy.is_alive() for enemy in enemies):
        for player in players:
            if player.hp > 0:
                # ✅ NEW: Check if all enemies are dead before player's turn
                if all(not enemy.is_alive() for enemy in enemies):
                    print("\n🎉 All enemies are defeated! 🎉")
                    return end_battle(players, return_after_battle)  # ✅ Fixed indentation

                print("\n📊 Current Status:")
                for p in players:
                    print(f"❤️ {p.name} HP: {p.hp}/{p.max_hp} | 🔥 Limit Break: {p.limit_break_meter}%")

                for e in enemies:
                    if e.is_alive():
                        print(f"💀 {e.name} HP: {e.hp}/{e.max_hp}")

                print(f"\n🎮 {player.name}'s Turn!")
                print("1. Attack")
                print("2. Cast Spell")
                print("3. Use Item")
                if player.limit_break_meter >= 100:
                    print("4. LIMIT BREAK! ⚡")

                choice = input("> ")

                if choice == "1":
                    target = choose_enemy(enemies)
                    if target:
                        player.attack_enemy(target)
                elif choice == "2":
                    player.cast_spell(players, enemies)
                elif choice == "3":
                    use_item(player)
                elif choice == "4" and player.limit_break_meter >= 100:
                    target = choose_enemy(enemies)
                    if target:
                        player.use_limit_break(target)
                else:
                    print("\n⚠️ Invalid choice. Try again.")

        # ✅ NEW: Re-check if all enemies are dead before enemy turn
        if all(not enemy.is_alive() for enemy in enemies):
            print("\n🎉 All enemies are defeated! 🎉")
            return end_battle(players, return_after_battle)

        # Enemies take their turns
        for enemy in enemies:
            if enemy.is_alive():
                enemy.enemy_attack(random.choice(players))

def choose_enemy(enemies):
    """Allows the player to select which enemy to attack, with validation."""
    valid_targets = [enemy for enemy in enemies if enemy.is_alive()]

    if not valid_targets:
        return None  # ✅ Prevents error when no enemies remain

    print("\n🎯 Choose an enemy to attack:")
    for i, enemy in enumerate(valid_targets, 1):
        print(f"{i}. {enemy.name} (HP: {enemy.hp}/{enemy.max_hp})")

    while True:
        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(valid_targets):
                return valid_targets[choice]
            else:
                print("\n⚠️ Invalid choice. Try again.")
        except ValueError:
            print("\n⚠️ Please enter a number corresponding to an enemy.")

def display_damage_animation():
    """Shows an ASCII animation for attacks."""
    time.sleep(0.2)
    print("\n💥 BOOM! 💥")
    time.sleep(0.3)

def use_item(player):
    """Allows the player to use an item from their inventory."""
    print("\n🎒 Choose an item to use:")
    
    item_list = list(player.items.keys())
    for i, item in enumerate(item_list, 1):
        print(f"{i}. {item} ({player.items[item]} left)")

    try:
        choice = int(input("> ")) - 1
        if 0 <= choice < len(item_list):
            item = item_list[choice]
            if item == "Potion":
                if player.hp < player.max_hp:
                    heal_amount = 30
                    player.hp = min(player.max_hp, player.hp + heal_amount)
                    player.items[item] -= 1
                    print(f"\n💖 {player.name} used a Potion! Restored {heal_amount} HP.")
                else:
                    print("\n⚠️ HP is already full!")
            elif item == "Ether":
                if player.mp < player.max_mp:
                    restore_mp = 15
                    player.mp = min(player.max_mp, player.mp + restore_mp)
                    player.items[item] -= 1
                    print(f"\n🔋 {player.name} used an Ether! Restored {restore_mp} MP.")
                else:
                    print("\n⚠️ MP is already full!")
        else:
            print("\n⚠️ Invalid choice.")
    except ValueError:
        print("\n⚠️ Please enter a valid number.")

def use_limit_break(self, target):
    """Executes a powerful Limit Break attack when the meter is full."""
    if self.limit_break_meter >= 100:
        print(f"\n⚡ {self.name} activates their LIMIT BREAK! ⚡")
        time.sleep(1)

        if self.name == "Cloud":
            damage = random.randint(50, 70)
            print("\n💥 BRAVER! 💥")
        elif self.name == "Barret":
            damage = random.randint(60, 80)
            print("\n💥 BIG SHOT! 💥")
        else:
            damage = random.randint(40, 60)
            print("\n💥 UNKNOWN LIMIT BREAK! 💥")

        target.hp -= damage
        self.limit_break_meter = 0  # Reset meter after using
        print(f"\n🔥 {self.name} deals {damage} damage to {target.name}!")

Character.use_limit_break = use_limit_break  # ✅ Add Limit Break to Character class dynamically

def end_battle(players, return_after_battle):
    """Ends the battle and returns to the next game phase."""
    print("\n🎉 You won the battle! 🎉")
    if return_after_battle:
        return_after_battle()
    else:
        print("\n📜 Do you want to open the menu?")
        print("1. Yes")
        print("2. No, continue")
        
        menu_choice = input("> ")
        if menu_choice == "1":
            open_menu()



  
 
 
 
  
 














