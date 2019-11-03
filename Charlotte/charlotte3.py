from robotlib import start, avance, recule, droite, gauche, objetdevant, objetderriere, stop, fin

# Comment programmer ton robot ?
#
# Tout d'abord, tu dois le demarrer en utilisant la fonction start()
#
# Ensuite tu peux:
#    Le faire avancer avec la fonction avance(). Tu dois indiquer entre les parantheses de la fonction le nombre de centimetres duquel doit avance le robot.
#       Par exemple, pour le faire avancer de 10 centimetres, tu dois ecrire avance(10)
#    Le faire tourner a droite avec la fonction droite(). Tu dois indiquer entre les parantheses de la fonction le nombre de degrees duquel doit tourner le robot.
#         Par exemple, pour le faire tourner d'un quart de tour (un angle droit) tu dois ecrire droite(90)
#    Le faire tourner a gauche avec la fonction gauche().
#         Comme pour la fonction droite, tu dois indiquer entre les parantheses de la fonction le nombre de degrees duquel doit tourner le robot
#    Le faire reculer avec la fonction recule().
#         Comme pour la fonction avance(), tu dois indiquer entre les parantheses de la fonction le nombre de centimetres duquel doit reculer le robot.
#    L'arreter avec la fonction stop()
#    Detecter un obstacle devant avec la fonction objetdevant(). Detecter un obstacle derriere avec la fonction objetderriere(). Ces fonctions necessite une condition.
#          Pour utiliserla condition, il faut utiliser le mot if (qui veut dire si en anglais)
#          Par exemple:
#              if objetdevant():
#                  stop()
#              else:
#                  avance(1)
#
# A la fin, tu dois arreter le robot en utilisant la fonction fin()

start()


while True:
    if objetdevant():
        if objetderriere():
            gauche(30)
        else:
            recule(20)
            gauche(90)
    else:
        avance(1)


fin()
