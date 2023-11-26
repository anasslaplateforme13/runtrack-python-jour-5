def parcours_toilette(nombre_marches, hauteur_marche):

    hauteur_marche = hauteur_marche / 100
    parcours = (nombre_marches * hauteur_marche) * 2
    parcours_semaine = parcours * 7

    print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcours {parcours_semaine:.2f} m par semaine.")
parcours_toilette(100, 11)