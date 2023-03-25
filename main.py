import requests

# Clé API
api_key = "e0a1bf2c844edb9084efc764c089dd748676cc14"
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
WARNING = '\033[93m'
# URL de l'API
url = "https://api.jcdecaux.com/vls/v1/"

#fonction pour récupérer les données d'une ville donnée
def afficher_données(ville):
    # Envoi d'une requête GET à l'API pour récupérer les données sur la ville
    response = requests.get(url + "stations?contract=" + ville + "&apiKey=" + api_key)
    # Vérification du statut de la réponse
    if response.status_code == 200:
        # Récupération des données de la réponse en format JSON
        stations = response.json()
        # Initialisation des compteurs pour les types de vélos
        velos_mecaniques = 0
        velos_electriques = 0
        # Boucle sur les stations pour compter les types de vélos
        for station in stations:
            velos_mecaniques += station["available_bikes"]
            velos_electriques += station["available_bike_stands"]
        print("Ville : ", ville, "Vélos mécaniques : ", str(velos_mecaniques), "Vélos électriques : ", str(velos_electriques))
        #afficher les pourcentages de vélos mécaniques et électriques avec des couleurs
        pourcentage_mecanique = (velos_mecaniques / (velos_mecaniques + velos_electriques)) * 100
        pourcentage_electrique = (velos_electriques / (velos_mecaniques + velos_electriques)) * 100

        #afficher sous forme de barre de plusieurs '#' en fonction du pourcentage
        print( OKBLUE + "#" * int(pourcentage_mecanique) + WARNING + "#" * int(pourcentage_electrique))
        #formater number avec 2 chiffres après la virgule
        pourcentage_mecanique = "{:.2f}".format(pourcentage_mecanique)
        pourcentage_electrique = "{:.2f}".format(pourcentage_electrique)
        print( OKBLUE + "(velos_mecaniques : ", pourcentage_mecanique, "%)", WARNING, "(velos_electriques : ", pourcentage_electrique, "%)", ENDC)
    else:
        #sinon retourne None
        print(FAIL + "Ville inconnue", ENDC)

print(OKGREEN + "Bienvenue dans l'application de vélos en libre service de JCDecaux", ENDC)
#demmande à l'utilisateur de saisir une ville oubien plusieurs villes séparées par des virgules oubien quitter
ville = input("Saisissez une ville ou plusieurs villes séparées par des virgules(,) ou tapez 'q' pour quitter : ")

#trim pour supprimer les espaces avant et après la saisie
ville = ville.strip()

#boucle tant que l'utilisateur ne tape pas 'q'
while ville != "q":
    #si l'utilisateur a saisi plusieurs villes
    if "," in ville:
        #on récupère les villes dans une liste
        villes = ville.split(",")
        #on boucle sur les villes
        for ville in villes:
            #on récupère les données de la ville
            data = afficher_données(ville)
    #si l'utilisateur a saisi une seule ville
    else:
        #on récupère les données de la ville
        data = afficher_données(ville)

    #on redemande à l'utilisateur de saisir une ville oubien plusieurs villes séparées par des virgules oubien quitter
    ville = input("Saisissez une ville ou plusieurs villes séparées par des virgules ou tapez 'q' pour quitter : ")
    ville = ville.strip()
