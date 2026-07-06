from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class SidePanel(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("SidePanel")

        self.setFixedWidth(280)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)

        layout.setSpacing(15)

        # --------------------------
        # Título
        # --------------------------

        titulo = QLabel("CONTROLE")

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(titulo)

        # --------------------------

        self.lblJogador = QLabel("👤 Jogador")

        layout.addWidget(self.lblJogador)

        self.lblPontos = QLabel("🏆 Pontos: 0")

        layout.addWidget(self.lblPontos)

        self.lblCategoria = QLabel("🎯 Categoria: ---")

        layout.addWidget(self.lblCategoria)

        self.lblPergunta = QLabel("❓ Pergunta: 0")

        layout.addWidget(self.lblPergunta)

        layout.addStretch()

        # --------------------------

        self.btGirar = QPushButton("🎡 GIRAR ROLETA")

        self.btGirar.setMinimumHeight(55)

        layout.addWidget(self.btGirar)