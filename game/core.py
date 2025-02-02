import random
import time

class Materia:
    """Represents materia that grants magic abilities and levels up."""
    def __init__(self, name, spell, min_damage, max_damage, mp_cost, is_support=False):
        self.name = name
        self.spell = spell
        self.is_support = is_support  
        self.mp_cost = mp_cost
        self.level = 1
        self.xp = 0
        self.xp_to_level = 30

        # Ensure all Materia has proper damage values
        if self.spell == "Cure":
            self.min_damage = min_damage  
            self.max_damage = max_damage
        else:
            self.min_damage = max(1, min_damage * 10)  # Ensuring at least 1 damage
            self.max_damage = max(5, max_damage * 12)

    def gain_xp(self):
        """Adds XP and levels up materia over time."""
        self.xp += 10
        if self.xp >= self.xp_to_level:
            self.level_up()

    def level_up(self):
        """Levels up the materia, increasing power and reducing MP cost."""
        self.level += 1
        self.xp -= self.xp_to_level
        self.xp_to_level = int(self.xp_to_level * 1.5)
        self.min_damage += 10
        self.max_damage += 12
        self.mp_cost = max(1, self.mp_cost - 1)  # Prevents negative MP cost

class Character:
    """Represents a character with stats, XP, Limit Breaks, and Materia system."""
    def __init__(self, name, hp, mp, attack, magic):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack = attack
        self.magic = magic
        self.level = 1
        self.xp = 0
        self.xp_to_level = 50  
        self.limit_break_meter = 0
        self.items = {"Potion": 3, "Ether": 2}  
        self.equipped_materia = []  
        self.equipped_support_materia = None  

    def equip_materia(self, materia):
        """Equips standard Materia (max 2 slots)."""
        if len(self.equipped_materia) < 2:
            self.equipped_materia.append(materia)
        else:
            print("\n⚠️ Cannot equip more than 2 Materia!")

    def equip_support_materia(self, materia):
        """Equips support Materia (only 1 slot)."""
        if materia.is_support:
            self.equipped_support_materia = materia
        else:
            print("\n⚠️ This is not a support Materia!")

    def attack_enemy(self, target):
        """Performs a basic attack with auto-targeting and crit chance."""
        if target.hp <= 0:
            print("\n⚠️ That enemy is already defeated! Choose another target.")
            return

        damage = random.randint(self.attack - 2, self.attack + 2)

        if random.random() < 0.15:  # 15% Critical Hit Chance
            damage = int(damage * random.uniform(1.5, 2.0))
            print(f"\n🔥 CRITICAL HIT! {self.name} deals {damage} damage!")

        target.hp -= damage
        print(f"\n⚔️ {self.name} attacks {target.name} for {damage} damage!")

        if target.hp <= 0:
            print(f"\n💀 {target.name} is defeated!")

    def cast_spell(self, allies, enemies):
        """Allows the player to select which Materia to use before casting."""
        if not self.equipped_materia:
            print("\n⚠️ No Materia equipped! Cannot cast magic.")
            return

        print("\n📜 Choose Materia to cast:")
        for i, materia in enumerate(self.equipped_materia, 1):
            print(f"{i}. {materia.name} ({materia.spell}) - MP Cost: {materia.mp_cost}")

        try:
            choice = int(input("> ")) - 1
            selected_materia = self.equipped_materia[choice]
        except (ValueError, IndexError):
            print("\n⚠️ Invalid selection. Cancelling spell.")
            return

        if self.mp < selected_materia.mp_cost:
            print("\n⚠️ Not enough MP to cast this spell!")
            return

        self.mp -= selected_materia.mp_cost  

        if selected_materia.spell == "Cure":
            print("\n👥 Choose an ally to heal:")
            for i, ally in enumerate(allies, 1):
                print(f"{i}. {ally.name} (HP: {ally.hp}/{ally.max_hp})")

            try:
                target = allies[int(input("> ")) - 1]
            except (ValueError, IndexError):
                print("\n⚠️ Invalid selection. Cancelling spell.")
                return

            heal_amount = random.randint(selected_materia.min_damage, selected_materia.max_damage)
            target.hp = min(target.max_hp, target.hp + heal_amount)
            print(f"\n💚 {self.name} casts {selected_materia.spell} on {target.name}, restoring {heal_amount} HP!")

        else:
            # ✅ If equipped with "All" Materia, attack all enemies
            if self.equipped_support_materia and self.equipped_support_materia.name == "All":
                print("\n⚡ Multi-target spell activated!")
                for enemy in enemies:
                    if enemy.hp > 0:
                        damage = random.randint(selected_materia.min_damage, selected_materia.max_damage)
                        enemy.hp -= damage
                        print(f"\n⚡ {self.name} casts {selected_materia.spell} on {enemy.name} for {damage} damage!")
            else:
                print("\n🎯 Choose an enemy to attack:")
                valid_targets = [enemy for enemy in enemies if enemy.hp > 0]
                for i, enemy in enumerate(valid_targets, 1):
                    print(f"{i}. {enemy.name} (HP: {enemy.hp}/{enemy.max_hp})")

                try:
                    target = valid_targets[int(input("> ")) - 1]
                except (ValueError, IndexError):
                    print("\n⚠️ Invalid selection. Cancelling spell.")
                    return

                damage = random.randint(selected_materia.min_damage, selected_materia.max_damage)
                target.hp -= damage
                print(f"\n⚡ {self.name} casts {selected_materia.spell} on {target.name} for {damage} damage!")



