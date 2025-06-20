# open sert a créer un fichier
# w+ sert a modifier un fichier
# r sert a lire un fichier
# a+ sert a ajouter un contenu dans un fichier
with open("meals.txt", "+r") as file:
    print(f"\n {file.readlines()}")
