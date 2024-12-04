def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name, damage=0, defensePower=0):
    return dict(
        name=name,
        score=0,
        damage=damage,
        health=100,
        defensePower=defensePower,
        defense=False,
    )

def addPlayer(player):
    global PlayerList
    PlayerList.append(player)

def removePlayer(name):
    global PlayerList
    for player in PlayerList:
        if player["name"] == name:
            PlayerList.remove(player)
            return
    print("There is no player with that name!")

def setPlayer(player, key, value):
    player[key] = value

def attackPlayer(attacker, target):
    if target["defense"]:
        damage = max(0, attacker["damage"] - target["defensePower"])
        setPlayer(target, "defense", False)  
        tambah = 0.8 
    else:
        damage = attacker["damage"]
        tambah = 1  
   
    setPlayer(target, "health", target["health"] - damage)
    setPlayer(attacker, "score",attacker["score"]  + tambah)

def displayMatchResult():
    global PlayerList
    PlayerList.sort(key=lambda x: (-x["score"], -x["health"]))

    for i, player in enumerate(PlayerList, start=1):
        print(f"Rank {i}: {player['name']} | Score: {player['score']} | Health: {player['health']}")
