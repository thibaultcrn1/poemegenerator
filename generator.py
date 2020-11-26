# Import de la fonction random dans le programme.
import random

# Affichage du design au lancement du programme.
print("================[FR]================")
print("==         Générateur de          ==")
print("==            Poème               ==")
print("====================================")
print()

# Zone d'écriture pour l'intéraction avec le programme.
response = float(input("Que voulez-vous comme poème ? Syntaxe: 4444 ou 4433"))
print()

# Création de la liste de vers pour les poèmes aléatoire.
list1 = [
    "test1",
    "test2",
    "test3",
    "test4"
]

# Condition qui détecte si le résultat écrit dans la zone d'écriture ci-dessus est égal à 4444
if response == 4444:
    # permet l'affichage en ligne + le mélange avec la fonction random de la liste ci dessus.
    print('\n'.join(random.sample(list1, 4)))
    # permet de faire un espace entre chaque strophe.
    print()
    print('\n'.join(random.sample(list1, 4)))
    print()
    print('\n'.join(random.sample(list1, 4)))
    print()
    print('\n'.join(random.sample(list1, 4)))

# Condition qui permet d'afficher un message d'erreur si un autre nombre que 4444 ou 4433 est écrit dans la zone
# d'intéraction.
else:
    print("[ERREUR] Vous avez écrit des caractères qui ne sont pas valide !")

# Condition qui détecte si le résultat écrit dans la zone d'écriture ci-dessus est égal à 4433
if response == 4433:
    # permet l'affichage en ligne + le mélange avec la fonction random de la liste ci dessus.
    print('\n'.join(random.sample(list1, 4)))
    print()
    print('\n'.join(random.sample(list1, 4)))
    print()
    print('\n'.join(random.sample(list1, 3)))
    print()
    print('\n'.join(random.sample(list1, 3)))
