import time
from game import *

initPlayers()

hehe = createNewPlayer(name="hehe", damage=20, defensePower=5)
pua = createNewPlayer(name="pua", damage=15, defensePower=10)
lee = createNewPlayer(name="Lee", damage=25, defensePower=7)
sang_legenda = createNewPlayer(name="Sang Legenda", damage=30, defensePower=8)

addPlayer(hehe)
addPlayer(pua)
addPlayer(lee)
addPlayer(sang_legenda)

print("=== Simulasi Game Dimulai ===\n")

print("hehe menyerang Lee:")
attackPlayer(hehe, lee)
print(f"Lee's Health: {lee['health']}, hehe Score: {hehe['score']}\n")
time.sleep(1)

print("pua menyerang Sang Legenda:")
attackPlayer(pua, sang_legenda)
print(f"Sang Legenda's Health: {sang_legenda['health']}, pua Score: {pua['score']}\n")
time.sleep(1)

setPlayer(hehe, "defense", True)
attackPlayer(sang_legenda, hehe)
print(f"hehe's Health: {hehe['health']}, Sang Legenda Score: {sang_legenda['score']}\n")
time.sleep(1)

print("hehe menyerang pua:")
attackPlayer(hehe, pua)
print(f"pua's Health: {pua['health']}, hehe Score: {hehe['score']}\n")
time.sleep(1)

print("Lee menyerang Sang Legenda (Sang Legenda dalam mode defense):")
setPlayer(sang_legenda, "defense", True)
attackPlayer(lee, sang_legenda)
print(f"Sang Legenda's Health: {sang_legenda['health']}, Lee Score: {lee['score']}\n")
time.sleep(1)

print("pua menyerang hehe yang sudah lemah:")
attackPlayer(pua, hehe)
print(f"hehe's Health: {hehe['health']}, pua Score: {pua['score']}\n")
time.sleep(1)

print("=== Hasil Akhir Pertandingan ===")
displayMatchResult()
