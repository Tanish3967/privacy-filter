from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPainter, QBrush, QRadialGradient, QCursor
from PySide6.QtCore import Qt, QTimer
import sys

class PrivacyFilter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Privacy Filter")
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool |
            Qt.WindowTransparentForInput
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.showFullScreen()

        # Update display frequently (every 50ms) to track cursor movement
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(50)

    def paintEvent(self, event):
        painter = QPainter(self)
        width, height = self.width(), self.height()
        local_cursor = self.mapFromGlobal(QCursor.pos())

        # 1) Draw a radial gradient from the center, transparent in the middle and black at the edges
        center_x, center_y = width / 2, height / 2
        base_gradient = QRadialGradient(center_x, center_y, max(width, height) / 2)
        base_gradient.setColorAt(0.0, Qt.transparent)
        base_gradient.setColorAt(1.0, Qt.black)

        painter.setBrush(QBrush(base_gradient))
        painter.setPen(Qt.NoPen)
        painter.drawRect(0, 0, width, height)

        # 2) If the cursor is near any edge, clear a circular area around the cursor
        #    Distance from edges: left (x), right (width - x), top (y), bottom (height - y)
        distance_to_edge = min(
            local_cursor.x(),
            width - local_cursor.x(),
            local_cursor.y(),
            height - local_cursor.y()
        )

        # Adjust these thresholds/radius to taste
        threshold = 200  # How close to the edge before clearing is activated
        clear_radius = 150

        if distance_to_edge < threshold:
            # Switch to Clear mode to erase the overlay in a circle around the cursor
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.drawEllipse(local_cursor, clear_radius, clear_radius)
            # Restore the painter mode
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrivacyFilter()
    window.show()
    sys.exit(app.exec())
