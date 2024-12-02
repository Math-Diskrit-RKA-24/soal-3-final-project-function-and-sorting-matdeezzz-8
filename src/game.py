def initPlayers() :
  
  global PlayerList
  PlayerList = []
  
def createNewPlayer(name, damage=0, defensePower=0) :
  
  return {name = name, 
          score = 0, 
          damage = damage, 
          health =100,
          defensePower = defensePower,
          defense = false }
 
def addPlayer(player) : 
  
  global PlayerList
  PlayerList.append(player)
    
def removePlayer(name) :
  global PlayerList[]
  for Player in PlayerList :
    if Player['name'] = name :
      return Playerlist.remove(player) 
  return "There is no player with that name!"

def setPlayer(player, key, value) :
  
  player[key] = value

def attackPlayer(attacker:dict, target:dict) :
  if target['defense'] :
    damage = max(0,attacker[attack] - target[defense_strenght]) 
    setPlayer (target, 'defense', False) 
  else : 
    damage = attacker[attack]
    setPlayer (target, 'health", True)
    setPlayer(attacker, "score", attacker["score"] + 1)
  
def displayMatchResult() :
  return PlayerList.sort(Reverse = True,key =Player['name'] and Player['score']  and Player['health'] )
