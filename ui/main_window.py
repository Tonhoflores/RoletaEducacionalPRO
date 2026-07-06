from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt

from ui.styles import APP_STYLE
from ui.side_panel import SidePanel
from ui.wheel_widget import WheelWidget


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Roleta Educacional PRO")
        self.resize(1400, 850)

        self.setStyleSheet(APP_STYLE)

        self.criar_interface()

    def criar_interface(self):

        layout_principal = QHBoxLayout(self)

        layout_principal.setContentsMargins(15, 15, 15, 15)
        layout_principal.setSpacing(15)

        # =====================================
        # Área esquerda
        # =====================================

        esquerda = QVBoxLayout()

        titulo = QLabel("🎡 ROLETA EDUCACIONAL PRO")
        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        esquerda.addWidget(titulo)

        self.roleta = WheelWidget()
        esquerda.addWidget(self.roleta)

        status = QFrame()

        status.setFixedHeight(40)

        status_layout = QHBoxLayout(status)

        self.lblStatus = QLabel("Sistema iniciado")

        status_layout.addWidget(self.lblStatus)

        status_layout.addStretch()

        versao = QLabel("v0.1")

        versao.setAlignment(Qt.AlignRight)

        status_layout.addWidget(versao)

        esquerda.addWidget(status)

        layout_principal.addLayout(esquerda, 3)

        # =====================================
        # Painel lateral
        # =====================================

        self.painel = SidePanel()

        layout_principal.addWidget(self.painel, 1)

        # =====================================
        # Eventos
        # =====================================

        self.painel.btGirar.clicked.connect(self.girar)

    def girar(self):

        self.lblStatus.setText("Girando a roleta...")

        # A animação será implementada na Sprint 2