from robotlib import start, avance, recule, droite, gauche, stop, fin, objetdevant, objetderriere

start()

while True:
    if objetdevant():
        recule(6)
        gauche(90)
    else:
        avance(1)


fin()
