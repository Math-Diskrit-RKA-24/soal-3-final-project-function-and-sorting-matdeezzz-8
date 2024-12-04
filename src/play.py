##MAAF MAS KETIDURAN LUPA COMMIT

import tkinter as tk
from tkinter import simpledialog, messagebox
from game import *  

def rankPlayers():
    sorted_players = sorted(PlayerList, key=lambda player: player["health"], reverse=True)

    ranking_message = "=== Rankingnya b ===\n"
    for idx, player in enumerate(sorted_players, start=1):
        ranking_message += f"{idx}. {player['name']} - Health: {player['health']}\n"
    
    show_popup(ranking_message)
def show_popup(message):
    popup = tk.Toplevel()
    popup.title("simulasi game")
    label = tk.Label(popup, text=message)
    label.pack(padx=55, pady=55)
    button = tk.Button(popup, text="OK", command=popup.destroy)
    button.pack(pady=20)

def createPlayerMenu():
    name = simpledialog.askstring("Player Name", "Enter player name:")
    damage = simpledialog.askinteger("Damage", f"Enter damage for {name}:")
    defense = simpledialog.askinteger("Defense", f"Enter defense for {name}:")
    
    player = createNewPlayer(name, damage, defense)
    addPlayer(player)  
    
    print("Current PlayerList:", [player["name"] for player in PlayerList])  
    show_popup(f"Player {name} added successfully!")

def choose_target():
    if len(PlayerList) < 2:
        show_popup("Pemainnya ngga ada kocakk")
        return None, None

    player_names = [player["name"] for player in PlayerList]
    attacker_name = simpledialog.askstring("Select Attacker", "yang nyerang siapa " + ", ".join(player_names))

    if attacker_name not in player_names:
        show_popup("dia ngga ikut main")
        return None, None

    target_names = [player["name"] for player in PlayerList if player["name"] != attacker_name]
    target_name = simpledialog.askstring("Select Target", f"Targetnya siapa {attacker_name} from: " + ", ".join(target_names))

    if target_name not in target_names:
        show_popup("dia ngga ikut main")
        return None, None

    attacker = next(player for player in PlayerList if player["name"] == attacker_name)
    target = next(player for player in PlayerList if player["name"] == target_name)

    return attacker, target

def startGame():
    if len(PlayerList) < 2:
        show_popup("mau lawan siapa kocakk")
        return

    show_popup("Game Started!")

    while len(PlayerList) > 1:
        attacker, target = choose_target()
        
        if attacker is None or target is None:
            return 
        damage = max(attacker["damage"] - target["defense"], 0)
        target["health"] -= damage  
        
        message = f"{attacker['name']} nyerang {target['name']} dengan {damage} damage!"
        show_popup(message)

        if target["health"] <= 0:
            message = f"{target['name']} kalah hahahaha!"
            show_popup(message)
            removePlayer(target["name"])  
      
        result = "\n".join([f"{player['name']}: {player['health']} health" for player in PlayerList])
        show_popup(result)

    winner = PlayerList[0]  
    final_result = f"Game Over!\nWinner: {winner['name']}\nHealth: {winner['health']}\nScore: {winner['score']}"
    show_popup(final_result)

root = tk.Tk()
root.title("Simulasi Game")

create_player_button = tk.Button(root, text="Create Player", command=createPlayerMenu)
create_player_button.pack(pady=55)

start_game_button = tk.Button(root, text="Start Game", command=startGame)
start_game_button.pack(pady=55)

root.mainloop()
