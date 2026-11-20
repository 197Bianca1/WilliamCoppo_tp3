import random

from maya import cmds


class RandoAnimator:
    def __init__(self, ui):

        # on fait référence a l'UI pour pouvoir récupérer les valeurs des spinbox
        self.ui = ui

    def animator(self):

        # on récupère l'objet sélectionné dans Maya
        ob = cmds.ls(sl=True)

        if not ob:
            cmds.warning("Please select an object to animate.")
            return

        duration = self.ui.duration.value()
        interval = self.ui.interval.value()

        if duration <= 1 or interval <= 0:
            cmds.warning("Duration must be greater than 1 and interval must be positive.")
            return

        # Translate Min
        translate_min_x = self.ui.translate_min_x.value()
        translate_min_y = self.ui.translate_min_y.value()
        translate_min_z = self.ui.translate_min_z.value()

        # Translate Max
        translate_max_x = self.ui.translate_max_x.value()
        translate_max_y = self.ui.translate_max_y.value()
        translate_max_z = self.ui.translate_max_z.value()

        # Vérification des valeurs min et max pour la translation
        if (translate_min_x > translate_max_x or
            translate_min_y > translate_max_y or
            translate_min_z > translate_max_z):

            cmds.warning("Translate min values must be less than or equal to translate max values.")
            return

        # Rotation Min
        rotation_min_x = self.ui.rotation_min_x.value()
        rotation_min_y = self.ui.rotation_min_y.value()
        rotation_min_z = self.ui.rotation_min_z.value()

        # Rotation Max
        rotation_max_x = self.ui.rotation_max_x.value()
        rotation_max_y = self.ui.rotation_max_y.value()
        rotation_max_z = self.ui.rotation_max_z.value()

        # Vérification des valeurs min et max pour la rotation
        if(rotation_min_x > rotation_max_x or
           rotation_min_y > rotation_max_y or
           rotation_min_z > rotation_max_z):

            cmds.warning("Rotation min values must be less than or equal to rotation max values.")
            return

        # Scale Min
        scale_min_x = self.ui.scale_min_x.value()
        scale_min_y = self.ui.scale_min_y.value()
        scale_min_z = self.ui.scale_min_z.value()

        # Scale Max
        scale_max_x = self.ui.scale_max_x.value()
        scale_max_y = self.ui.scale_max_y.value()
        scale_max_z = self.ui.scale_max_z.value()

        if (scale_min_x > scale_max_x or
            scale_min_y > scale_max_y or
            scale_min_z > scale_max_z):
            
            cmds.warning("Scale min values must be less than or equal to scale max values.")
            return

        cmds.playbackOptions(min=1, max=duration)

        # Commencer le Undo
        cmds.undoInfo(openChunk=True, chunkName="Animation")

        try:
            for object in ob:

                # supprimer l'ancienne animation
                cmds.cutKey(object, clear=True)

                # générer les keys frame
                for frame in range(1, duration, interval):

                    # valeurs aléatoires pour la translation
                    translate_x = random.uniform(translate_min_x, translate_max_x)
                    translate_y = random.uniform(translate_min_y, translate_max_y)
                    translate_z = random.uniform(translate_min_z, translate_max_z)

                    # valeurs aléatoires pour la rotation
                    rotation_x = random.uniform(rotation_min_x, rotation_max_x)
                    rotation_y = random.uniform(rotation_min_y, rotation_max_y)
                    rotation_z = random.uniform(rotation_min_z, rotation_max_z)

                    # valeurs aléatoires pour le scale
                    scale_x = random.uniform(scale_min_x, scale_max_x)
                    scale_y = random.uniform(scale_min_y, scale_max_y)
                    scale_z = random.uniform(scale_min_z, scale_max_z)

                    # keyframe pour la translation
                    cmds.setKeyframe(object, attribute="translateX", value=translate_x, time=frame)
                    cmds.setKeyframe(object, attribute="translateY", value=translate_y, time=frame)
                    cmds.setKeyframe(object, attribute="translateZ", value=translate_z, time=frame)

                    # keyframe pour la rotation
                    cmds.setKeyframe(object, attribute="rotateX", value=rotation_x, time=frame)
                    cmds.setKeyframe(object, attribute="rotateY", value=rotation_y, time=frame)
                    cmds.setKeyframe(object, attribute="rotateZ", value=rotation_z, time=frame)

                    # keyframe pour le scale
                    cmds.setKeyframe(object, attribute="scaleX", value=scale_x, time=frame)
                    cmds.setKeyframe(object, attribute="scaleY", value=scale_y, time=frame)
                    cmds.setKeyframe(object, attribute="scaleZ", value=scale_z, time=frame)

                    if frame == 1:

                        # première frame de translation
                        first_translate_x = translate_x
                        first_translate_y = translate_y
                        first_translate_z = translate_z

                        # première frame de rotation
                        first_rotation_x = rotation_x
                        first_rotation_y = rotation_y
                        first_rotation_z = rotation_z

                        # première frame de scale
                        first_scale_x = scale_x
                        first_scale_y = scale_y
                        first_scale_z = scale_z

                # keyframe finale pour la translation
                cmds.setKeyframe(object, attribute="translateX", value=first_translate_x, time=duration)
                cmds.setKeyframe(object, attribute="translateY", value=first_translate_y, time=duration)
                cmds.setKeyframe(object, attribute="translateZ", value=first_translate_z, time=duration)

                # keyframe finale pour la rotation
                cmds.setKeyframe(object, attribute="rotateX", value=first_rotation_x, time=duration)
                cmds.setKeyframe(object, attribute="rotateY", value=first_rotation_y, time=duration)
                cmds.setKeyframe(object, attribute="rotateZ", value=first_rotation_z, time=duration)

                # keyframe finale pour le scale
                cmds.setKeyframe(object, attribute="scaleX", value=first_scale_x, time=duration)
                cmds.setKeyframe(object, attribute="scaleY", value=first_scale_y, time=duration)
                cmds.setKeyframe(object, attribute="scaleZ", value=first_scale_z, time=duration)

        finally:
            cmds.undoInfo(closeChunk=True)

        cmds.currentTime(1)
