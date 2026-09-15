import random

'''


⠀⠀⠀⠀⠀⠀         ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣶⡄
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡴⠖⢂⣽⣿⣿⣷⣔⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟
⠀⠀⠀⠀⣀⣤⡶⢿⣋⣥⣤⣶⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⡀⢀⣠⣾⠿⠋⠀
⠀⢀⣴⣿⠟⠉⠀⠀⠀⠈⠉⠛⠻⣿⣿⣿⣿⡿⠛⠋⠉⣀⣤⠶⠟⠋⠁⠀⠀⠀
⢰⣿⡟⠁⠀⠀⠀⣷⠀⠀⠀⠀⠀⠈⣿⣿⣟⣀⡤⠖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠿⣧⣀⡠⠤⢾⣿⣷⠤⠄⠀⠀⠀⢹⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠀⠀⠀⡿⠁⠀⠀⠀⠀⠀⠈⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


ad astra per aspera!



'''

WHOLE_DECK = [
    # major arcana
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "The Strength", "The Hermit",
    "The Wheel Of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World",
    
    # minor arcana
    "Wands1", "Wands2", "Wands3", "Wands4", "Wands5", "Wands6", "Wands7", "Wands8", "Wands9", "Wands10",
    "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands",
    "Cups1", "Cups2", "Cups3", "Cups4", "Cups5", "Cups6", "Cups7", "Cups8", "Cups9", "Cups10",
    "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups",
    "Swords1", "Swords2", "Swords3", "Swords4", "Swords5", "Swords6", "Swords7", "Swords8", "Swords9", "Swords10",
    "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords",
    "Pentacles1", "Pentacles2", "Pentacles3", "Pentacles4", "Pentacles5", "Pentacles6", "Pentacles7", "Pentacles8", "Pentacles9", "Pentacles10",
    "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles",
    
    # major arcana reversed
    "The Fool (Reversed)", "The Magician (Reversed)", "The High Priestess (Reversed)", "The Empress (Reversed)", "The Emperor (Reversed)",
    "The Hierophant (Reversed)", "The Lovers (Reversed)", "The Chariot (Reversed)", "The Strength (Reversed)", "The Hermit (Reversed)",
    "The Wheel Of Fortune (Reversed)", "Justice (Reversed)", "The Hanged Man (Reversed)", "Death (Reversed)", "Temperance (Reversed)",
    "The Devil (Reversed)", "The Tower (Reversed)", "The Star (Reversed)", "The Moon (Reversed)", "The Sun (Reversed)",
    "Judgement (Reversed)", "The World (Reversed)",
    
    # minor arcana reversed
    "Wands1 (Reversed)", "Wands2 (Reversed)", "Wands3 (Reversed)", "Wands4 (Reversed)", "Wands5 (Reversed)", "Wands6 (Reversed)", "Wands7 (Reversed)", "Wands8 (Reversed)", "Wands9 (Reversed)", "Wands10 (Reversed)",
    "Page of Wands (Reversed)", "Knight of Wands (Reversed)", "Queen of Wands (Reversed)", "King of Wands (Reversed)",
    "Cups1 (Reversed)", "Cups2 (Reversed)", "Cups3 (Reversed)", "Cups4 (Reversed)", "Cups5 (Reversed)", "Cups6 (Reversed)", "Cups7 (Reversed)", "Cups8 (Reversed)", "Cups9 (Reversed)", "Cups10 (Reversed)",
    "Page of Cups (Reversed)", "Knight of Cups (Reversed)", "Queen of Cups (Reversed)", "King of Cups (Reversed)",
    "Swords1 (Reversed)", "Swords2 (Reversed)", "Swords3 (Reversed)", "Swords4 (Reversed)", "Swords5 (Reversed)", "Swords6 (Reversed)", "Swords7 (Reversed)", "Swords8 (Reversed)", "Swords9 (Reversed)", "Swords10 (Reversed)",
    "Page of Swords (Reversed)", "Knight of Swords (Reversed)", "Queen of Swords (Reversed)", "King of Swords (Reversed)",
    "Pentacles1 (Reversed)", "Pentacles2 (Reversed)", "Pentacles3 (Reversed)", "Pentacles4 (Reversed)", "Pentacles5 (Reversed)", "Pentacles6 (Reversed)", "Pentacles7 (Reversed)", "Pentacles8 (Reversed)", "Pentacles9 (Reversed)", "Pentacles10 (Reversed)",
    "Page of Pentacles (Reversed)", "Knight of Pentacles (Reversed)", "Queen of Pentacles (Reversed)", "King of Pentacles (Reversed)"
]

while True:
    print("welcome to bugg's tarot deck!")
    user_action = input("write your question now, or don't. just type something to continue").lower()
    user_action = input("type DRAW to draw, or q to quit: ").lower()
    
    if user_action == "q":
        print("farewell!")
        break
    elif user_action == "draw":
        card = random.choice(WHOLE_DECK)
        print(f"you drew: {card}")
    else:
        print("invalid action! type DRAW or q.")