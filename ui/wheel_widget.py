import math

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import (
    QColor,
    QPainter,
    QPen,
    QFont,
    QPolygonF
)
from PySide6.QtWidgets import QWidget


class WheelWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(650, 650)

        self.angle = 0

        self.categories = [
            "Matemática",
            "Português",
            "História",
            "Geografia",
            "Inglês",
            "Química",
            "Biologia",
            "Física"
        ]

        self.colors = [
            "#FF595E",
            "#FFCA3A",
            "#8AC926",
            "#1982C4",
            "#6A4C93",
            "#F72585",
            "#00B4D8",
            "#FB8500"
        ]

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()

        cx = w / 2
        cy = h / 2

        radius = min(w, h) / 2 - 20

        total = len(self.categories)
        angle = 360 / total

        # Desenha os setores
        for i in range(total):

            painter.setBrush(QColor(self.colors[i]))
            painter.setPen(QPen(Qt.white, 2))

            start = (90 - self.angle - (i + 1) * angle) * 16

            painter.drawPie(
                int(cx - radius),
                int(cy - radius),
                int(radius * 2),
                int(radius * 2),
                int(start),
                int(angle * 16)
            )

        # Centro
        painter.setBrush(Qt.white)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(
            int(cx - 18),
            int(cy - 18),
            36,
            36
        )

        # Textos
        painter.setFont(QFont("Segoe UI", 10, QFont.Bold))
        painter.setPen(Qt.black)

        for i, texto in enumerate(self.categories):

            ang = math.radians(
                self.angle + i * angle + angle / 2
            )

            tx = cx + math.cos(math.radians(90) - ang) * radius * 0.63
            ty = cy - math.sin(math.radians(90) - ang) * radius * 0.63

            painter.save()

            painter.translate(tx, ty)

            painter.rotate(-(i * angle))

            painter.drawText(-45, 5, texto)

            painter.restore()

        # Ponteiro
        painter.setBrush(Qt.red)
        painter.setPen(Qt.NoPen)

        ponteiro = QPolygonF([
            QPointF(cx, 8),
            QPointF(cx - 15, 40),
            QPointF(cx + 15, 40)
        ])

        painter.drawPolygon(ponteiro)