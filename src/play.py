import time
from game import initPlayers, createNewPlayer, addPlayer, attackPlayer, setPlayer, displayMatchResult

initPlayers()

handoko = createNewPlayer(name="Handoko", damage=20, defensePower=5)
susi = createNewPlayer(name="Susi", damage=15, defensePower=10)
lee = createNewPlayer(name="Lee", damage=25, defensePower=7)
sang_legenda = createNewPlayer(name="Sang Legenda", damage=30, defensePower=8)

addPlayer(handoko)
addPlayer(susi)
addPlayer(lee)
addPlayer(sang_legenda)

print("=== Simulasi Game Dimulai ===\n")

print("Handoko menyerang Lee:")
attackPlayer(handoko, lee)
print(f"Lee's Health: {lee['health']}, Handoko's Score: {handoko['score']}\n")
time.sleep(1)

print("Susi menyerang Sang Legenda:")
attackPlayer(susi, sang_legenda)
print(f"Sang Legenda's Health: {sang_legenda['health']}, Susi's Score: {susi['score']}\n")
time.sleep(1)

setPlayer(handoko, "defense", True)
attackPlayer(sang_legenda, handoko)
print(f"Handoko's Health: {handoko['health']}, Sang Legenda's Score: {sang_legenda['score']}\n")
time.sleep(1)

print("Handoko menyerang Susi:")
attackPlayer(handoko, susi)
print(f"Susi's Health: {susi['health']}, Handoko's Score: {handoko['score']}\n")
time.sleep(1)

print("Lee menyerang Sang Legenda (Sang Legenda dalam mode defense):")
setPlayer(sang_legenda, "defense", True)
attackPlayer(lee, sang_legenda)
print(f"Sang Legenda's Health: {sang_legenda['health']}, Lee's Score: {lee['score']}\n")
time.sleep(1)

print("Susi menyerang Handoko yang sudah lemah:")
attackPlayer(susi, handoko)
print(f"Handoko's Health: {handoko['health']}, Susi's Score: {susi['score']}\n")
time.sleep(1)

print("=== Hasil Akhir Pertandingan ===")
displayMatchResult()

