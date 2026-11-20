from PySide6 import QtWidgets

class RandoAnimatorUI(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        # met en place le layout principal
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(4)

        # met en place le nom de la première partie de l'UI
        timing_group = QtWidgets.QGroupBox("Animation Timing")
        timing_layout = QtWidgets.QHBoxLayout(timing_group)

        # met en place les spinbox pour la durée
        self.duration = QtWidgets.QSpinBox()
        self.duration.setRange(2, 10000)
        self.duration.setValue(100)

        # met en place les spinbox pour l'intervalle
        self.interval = QtWidgets.QSpinBox()
        self.interval.setRange(1, 1000)
        self.interval.setValue(30)

        # met en place les labels et ajoute les spinbox au layout pour la durée
        timing_layout.addWidget(
            QtWidgets.QLabel("Duration (Frames):")
        )
        timing_layout.addWidget(self.duration)

        # met en place les labels et ajoute les spinbox au layout pour l'intervalle
        timing_layout.addWidget(
            QtWidgets.QLabel("Step (Frames):")
        )
        timing_layout.addWidget(self.interval)

        # ajoute le groupbox au layout principal
        layout.addWidget(timing_group)

        # ajoute un groupbox pour les paramètres de translation
        timing_group2 = QtWidgets.QGroupBox("translate parameters")
        timing_layout2 = QtWidgets.QHBoxLayout(timing_group2)

        # ajoute les spinbox pour les paramètres de translation minimum en x
        self.translate_max_x = QtWidgets.QDoubleSpinBox()
        self.translate_max_x.setRange(-1000, 1000)
        self.translate_max_x.setValue(0)

        # met en place les spinbox pour les paramètres de translation minimume en y
        self.translate_max_y = QtWidgets.QDoubleSpinBox()
        self.translate_max_y.setRange(-1000, 1000)
        self.translate_max_y.setValue(0)

        # met en place les spinbox pour les paramètres de translation minimum en z
        self.translate_max_z = QtWidgets.QDoubleSpinBox()
        self.translate_max_z.setRange(-1000, 1000)
        self.translate_max_z.setValue(0)

        # met en place les spinbox pour les paramètres de translation minimum en x
        self.translate_min_x = QtWidgets.QDoubleSpinBox()
        self.translate_min_x.setRange(-1000, 1000)
        self.translate_min_x.setValue(0)

        # met en place les spinbox pour les paramètres de translation minimum en y
        self.translate_min_y = QtWidgets.QDoubleSpinBox()
        self.translate_min_y.setRange(-1000, 1000)
        self.translate_min_y.setValue(0)

        # met en place les spinbox pour les paramètres de translation minimum en z
        self.translate_min_z = QtWidgets.QDoubleSpinBox()
        self.translate_min_z.setRange(-1000, 1000)
        self.translate_min_z.setValue(0)

        # ajoute les labels et ajoute les spinbox au layout minimum x
        timing_layout2.addWidget(
            QtWidgets.QLabel("min_x:")
        )
        timing_layout2.addWidget(self.translate_min_x)

        # ajoute les labels et ajoute les spinbox au layout minimum y
        timing_layout2.addWidget(
            QtWidgets.QLabel("min_y:")
        )
        timing_layout2.addWidget(self.translate_min_y)

        # ajoute les labels et ajoute les spinbox au layout minimum z
        timing_layout2.addWidget(
            QtWidgets.QLabel("min_z:")
        )
        timing_layout2.addWidget(self.translate_min_z)

        # ajoute les labels et ajoute les spinbox au layout maximum x
        timing_layout2.addWidget(
            QtWidgets.QLabel("max_x:")
                )
        timing_layout2.addWidget(self.translate_max_x)

        # ajoute les labels et ajoute les spinbox au layout maximum y
        timing_layout2.addWidget(
                    QtWidgets.QLabel("max_y:")
                )
        timing_layout2.addWidget(self.translate_max_y)

        # ajoute les labels et ajoute les spinbox au layout maximum z
        timing_layout2.addWidget(
                    QtWidgets.QLabel("max_z:")
                )
        timing_layout2.addWidget(self.translate_max_z)

        # ajoute le groupbox au layout principal
        layout.addWidget(timing_group2)

        # ajoute un groupbox pour les paramètres de rotation
        rotation_group = QtWidgets.QGroupBox("rotation parameters")
        rotation_layout = QtWidgets.QHBoxLayout(rotation_group)

        # ajoute les spinbox pour les paramètres de rotation maximum en x
        self.rotation_max_x = QtWidgets.QDoubleSpinBox()
        self.rotation_max_x.setRange(-360, 360)
        self.rotation_max_x.setValue(0)

        # ajoute les spinbox pour les paramètres de rotation maximum en y
        self.rotation_max_y = QtWidgets.QDoubleSpinBox()
        self.rotation_max_y.setRange(-360, 360)
        self.rotation_max_y.setValue(0)

        # ajoute les spinbox pour les paramètres de rotation maximum en z
        self.rotation_max_z = QtWidgets.QDoubleSpinBox()
        self.rotation_max_z.setRange(-360, 360)
        self.rotation_max_z.setValue(0)

        # ajoute les spinbox pour les paramètres de rotation minimum en x
        self.rotation_min_x = QtWidgets.QDoubleSpinBox()
        self.rotation_min_x.setRange(-360, 360)
        self.rotation_min_x.setValue(0)

        # ajoute les spinbox pour les paramètres de rotation minimum en y      
        self.rotation_min_y = QtWidgets.QDoubleSpinBox()
        self.rotation_min_y.setRange(-360, 360)
        self.rotation_min_y.setValue(0)

        # ajoute les spinbox pour les paramètres de rotation minimum en z
        self.rotation_min_z = QtWidgets.QDoubleSpinBox()
        self.rotation_min_z.setRange(-360, 360)
        self.rotation_min_z.setValue(0)

        # ajoute les labels et ajoute les spinbox au layout minimum x
        rotation_layout.addWidget(
            QtWidgets.QLabel("min_x:")
        )
        rotation_layout.addWidget(self.rotation_min_x)

        # ajoute les labels et ajoute les spinbox au layout minimum y
        rotation_layout.addWidget(
            QtWidgets.QLabel("min_y:")
        )
        rotation_layout.addWidget(self.rotation_min_y)

        # ajoute les labels et ajoute les spinbox au layout minimum z
        rotation_layout.addWidget(
            QtWidgets.QLabel("min_z:")
        )
        rotation_layout.addWidget(self.rotation_min_z)

        # ajoute les labels et ajoute les spinbox au layout maximum x
        rotation_layout.addWidget(
            QtWidgets.QLabel("max_x:")
        )
        rotation_layout.addWidget(self.rotation_max_x)

        # ajoute les labels et ajoute les spinbox au layout maximum y
        rotation_layout.addWidget(
            QtWidgets.QLabel("max_y:")
            )
        rotation_layout.addWidget(self.rotation_max_y)

        # ajoute les labels et ajoute les spinbox au layout maximum z        
        rotation_layout.addWidget(
            QtWidgets.QLabel("max_z:")
            )
        rotation_layout.addWidget(self.rotation_max_z)

        # ajoue du group box au layout principale
        layout.addWidget(rotation_group)

        # créé un groue box pour la size
        scale_group = QtWidgets.QGroupBox("scale parameters")
        scale_layout = QtWidgets.QHBoxLayout(scale_group)

        # met en place la size pour le x maximume
        self.scale_max_x = QtWidgets.QDoubleSpinBox()
        self.scale_max_x.setRange(1, 1000)
        self.scale_max_x.setValue(1)

        # met en place la size pour le y maximume 
        self.scale_max_y = QtWidgets.QDoubleSpinBox()
        self.scale_max_y.setRange(1, 1000)
        self.scale_max_y.setValue(1)

        # met en place la size pour le z maximume
        self.scale_max_z = QtWidgets.QDoubleSpinBox()
        self.scale_max_z.setRange(1, 1000)
        self.scale_max_z.setValue(1)

        # met en place la size pour le x minimume
        self.scale_min_x = QtWidgets.QDoubleSpinBox()
        self.scale_min_x.setRange(1, 1000)
        self.scale_min_x.setValue(1)

        # met en place la size pour le y minimume
        self.scale_min_y = QtWidgets.QDoubleSpinBox()
        self.scale_min_y.setRange(1, 1000)
        self.scale_min_y.setValue(1)

        # met en place la size pour le z minimume        
        self.scale_min_z = QtWidgets.QDoubleSpinBox()
        self.scale_min_z.setRange(1, 1000)
        self.scale_min_z.setValue(1)

        # ajoute les labels et ajoute les spinbox au layout minimum x
        scale_layout.addWidget(
            QtWidgets.QLabel("min_x:")
        )
        scale_layout.addWidget(self.scale_min_x)

        # ajoute les labels et ajoute les spinbox au layout minimum y
        scale_layout.addWidget(
            QtWidgets.QLabel("min_y:")
        )
        scale_layout.addWidget(self.scale_min_y)

        # ajoute les labels et ajoute les spinbox au layout minimum z
        scale_layout.addWidget(
            QtWidgets.QLabel("min_z:")
        )
        scale_layout.addWidget(self.scale_min_z)

        # ajoute les labels et ajoute les spinbox au layout maximum x
        scale_layout.addWidget(
            QtWidgets.QLabel("max_x:")
        )
        scale_layout.addWidget(self.scale_max_x)

        # ajoute les labels et ajoute les spinbox au layout maximum y
        scale_layout.addWidget(
            QtWidgets.QLabel("max_y:")
        )
        scale_layout.addWidget(self.scale_max_y)

        # ajoute les labels et ajoute les spinbox au layout maximum z
        scale_layout.addWidget(
            QtWidgets.QLabel("max_z:")
        )
        scale_layout.addWidget(self.scale_max_z)
        
        # ajoue du group box au layout principale
        layout.addWidget(scale_group)

        # création du bouton pour l'animation
        self.button = QtWidgets.QPushButton("Generate")
        self.button.setFixedSize(100,30)
       
        #créé le layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        #ajoute un bouton dans le layou
        button_layout.addWidget(self.button)

        #ajoute le layout du bouton dans le layout
        layout.addLayout(button_layout)
     