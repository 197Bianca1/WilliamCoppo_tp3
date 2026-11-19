
import os
import sys
import importlib

# on a obtenu le folder dans lequel il y a notre fichier courant
# __file__ = le fichier courant
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)

print(absolute_file_path)

# ici on vient ajouter absolute_folder_path au path de Python pour qu'il trouve les fichiers
sys.path.append(absolute_folder_path)

import ui
import animator

importlib.reload(ui)
importlib.reload(animator)


def main():
    global tool_window
    global random_animation_ui
    global random_animation_animator

    try:
        tool_window.close()
    except Exception:
        pass

    random_animation_ui = ui.RandoAnimatorUI()

    # créer l'animateur
    random_animation_animator = animator.RandoAnimator(random_animation_ui)

    # connecter le bouton à la méthode animator
    random_animation_ui.button.clicked.connect(
        random_animation_animator.animator
    )

    random_animation_ui.show()

    tool_window = random_animation_ui


main()