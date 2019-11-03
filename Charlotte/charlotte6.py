from robotlib import start, avance, recule, droite, gauche, objetdevant, objetderriere, stop, fin


start()

while True:
    gauche(1080)
    recule(20)
    avance(20)
    droite(1080)
    avance(20)
    recule(20)
    droite(90)
    gauche(90)
    recule(90)

fin()
