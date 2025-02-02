from game.core import Character, Materia  # ✅ Now importing from core.py, no circular import

# ✅ Define Materia
thunder_materia = Materia("Thunder", "Thunder", 3, 8, 5)
restore_materia = Materia("Restore", "Cure", -30, -50, 4)

# ✅ Cloud starts with Thunder & Restore Materia
cloud = Character("Cloud", hp=100, mp=30, attack=10, magic=12)
cloud.equip_materia(thunder_materia)  
cloud.equip_materia(restore_materia)  

# ✅ Barret has no Materia
barret = Character("Barret", hp=120, mp=20, attack=12, magic=8)


