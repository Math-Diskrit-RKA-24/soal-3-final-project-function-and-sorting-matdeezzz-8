import time
from game import initPlayers, createNewPlayer, addPlayer, attackPlayer, setPlayer, displayMatchResult

initPlayers()

hehe = createNewPlayer(name="Handoko", damage=20, defensePower=5)
pua = createNewPlayer(name="Susi", damage=15, defensePower=10)
lee = createNewPlayer(name="Lee", damage=25, defensePower=7)
sang_legenda = createNewPlayer(name="Sang Legenda", damage=30, defensePower=8)

addPlayer(hehe)
addPlayer(pua)
addPlayer(lee)
addPlayer(sang_legenda)

print("=== Simulasi Game Dimulai ===\n")

print("Handoko menyerang Lee:")
attackPlayer(hehe, lee)
print(f"Lee's Health: {lee['health']}, Handoko's Score: {hehe['score']}\n")
time.sleep(1)

print("Susi menyerang Sang Legenda:")
attackPlayer(pua, sang_legenda)
print(f"Sang Legenda's Health: {sang_legenda['health']}, Susi's Score: {pua['score']}\n")
time.sleep(1)

setPlayer(hehe, "defense", True)
attackPlayer(sang_legenda, hehe)
print(f"Handoko's Health: {hehe['health']}, Sang Legenda's Score: {sang_legenda['score']}\n")
time.sleep(1)

print("Handoko menyerang Susi:")
attackPlayer(hehe, pua)
print(f"Susi's Health: {pua['health']}, Handoko's Score: {hehe['score']}\n")
time.sleep(1)

print("Lee menyerang Sang Legenda (Sang Legenda dalam mode defense):")
setPlayer(sang_legenda, "defense", True)
attackPlayer(lee, sang_legenda)
print(f"Sang Legenda's Health: {sang_legenda['health']}, Lee's Score: {lee['score']}\n")
time.sleep(1)

print("Susi menyerang Handoko yang sudah lemah:")
attackPlayer(pua, hehe)
print(f"Handoko's Health: {hehe['health']}, Susi's Score: {pua['score']}\n")
time.sleep(1)

print("=== Hasil Akhir Pertandingan ===")
displayMatchResult()
