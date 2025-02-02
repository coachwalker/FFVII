import time
from game.reactor import reactor_mission

def display_intro():
    """Displays the ASCII intro before the game starts."""
    print("\n")
    print("███████╗███████╗██╗   ██╗██╗██╗ ")
    print("██╔════╝██╔════╝██║   ██║██║██║ ")
    print("█████╗  █████╗  ██║   ██║██║██║ ")
    print("██╔══╝  ██╔══╝  ╚██╗ ██╔╝╚═╝╚═╝ ")
    print("██║     ██║      ╚████╔╝  ██╗██╗ ")
    print("╚═╝     ╚═╝       ╚═══╝   ╚═╝╚═╝ ")
    print("\n🎮 Welcome to **Midgar Universe!**\n")
    time.sleep(2)  # ✅ Short delay so the intro is visible before mission text

def main():
    """Main game sequence. Starts in the reactor mission."""
    display_intro()  # ✅ Ensures ASCII intro appears before the mission starts
    reactor_mission()  # ✅ Starts the game directly in the reactor mission

if __name__ == "__main__":
    main()


