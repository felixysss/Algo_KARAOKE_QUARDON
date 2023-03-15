import random

class Player:
    def __init__(self, name, score):
        self.__nom= name
        self.__score= score
        self.__scoreTotal= scoreTotal
        self.__scoreMoyenne= scoreMoyenne
        self.__scoreMeilleur= scoreMeilleur
        self.__scorePire= scorePire
        def getNom(self):
            return self.__nom


def getMoyenne(score):
    return sum(score) / len(score)
    
def getTotal(score):
    return sum(score)

def getMeilleur(score):
    maxi = score[0]
    longueur=len(score)
    indice_max = 0
    for i in range(longueur):
        if score[i] >= maxi:
            maxi = score[i]
            indice_max = i
    return indice_max

def getPire(score):
    maxi = score[0]
    longueur=len(score)
    indice_max = 0
    for i in range(longueur):
        if score[i] <= maxi:
            maxi = score[i]
            indice_max = i
    return indice_max

nomJoueur= " "
scoreJoueur= 0
score= [0,0,0,0,0]
scoreTotal= getTotal(score)
scoreMoyenne = getMoyenne(score)
scoreMeilleur= getMeilleur(score)
scorePire= getPire(score)
chanson= 0


print("Quel est votre pseudo ?")
touche = input()
nomJoueur= input()
nomJoueur=touche

print(nomJoueur,", quelle chanson voulez-vous chanter ?")
touche = input()
chanson=input()
chanson=touche

scoreJoueur = random.randint(50,100)
print(nomJoueur, "votre score est de", scoreJoueur, ".")
score.pop(chanson)#ça ne marche pas
score.insert(chanson,scoreJoueur)#ça ne marche pas :(



print(nomJoueur, ", que voulez-vous voir ? A-Moyenne B-Total C-Meilleur D-Pire")
touche = input()

if (touche == 'A'):
    print (nomJoueur,", la moyenne de vos scores enregistrés est de", round(scoreMoyenne), ".")
    input()

if (touche == 'B'):
    print(nomJoueur,", le total de vos scores est de", scoreTotal,".")

if (touche == 'C'):
    print(nomJoueur,", votre meilleur score est celui de la chanson numéro", scoreMeilleur, ".")

if (touche == 'D'):
    print(nomJoueur,", votre pire score est celui de la chanson numéro", scorePire,".")
