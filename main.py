
import os
import sys
import importlib

# on a obtenu le folder dans lequel il y a notre fichier courant
# __file__ = le fichier courant
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)

# on affiche le chemin du fichier courant pour vérifier que c'est bien celui qu'on veut
print(absolute_file_path)

# ici on vient ajouter absolute_folder_path au path de Python pour qu'il trouve les fichiers
sys.path.append(absolute_folder_path)

import ui
import animator

importlib.reload(ui)
importlib.reload(animator)


def main():
    #déclare les varivale comme golbal pour pouvoir les utiliser dans d'autres fonctions
    global tool_window
    global random_animation_ui
    global random_animation_animator

    # on essaye de fermer la fenêtre si elle est déjà ouverte
    try:
        tool_window.close()
    except Exception:

        # on ne fait rien si la fenêtre n'existe pas encore
        pass

    # créer l'UI
    random_animation_ui = ui.RandoAnimatorUI()

    # créer l'animateur
    random_animation_animator = animator.RandoAnimator(random_animation_ui)

    # connecter le bouton à la méthode animator
    random_animation_ui.button.clicked.connect(
        random_animation_animator.animator
    )

    # affiche la fenetre
    random_animation_ui.show()

    #
    tool_window = random_animation_ui


main()