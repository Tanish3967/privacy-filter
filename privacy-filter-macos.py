from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPainter, QBrush, QRadialGradient, QCursor
from PySide6.QtCore import Qt, QTimer, QRect
import sys

class PrivacyFilter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Privacy Filter")
        
        # macOS-compatible window flags
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.showFullScreen()  # Cover full screen

        # Timer to update cursor position dynamically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(50)  # Update every 50ms
    
    def paintEvent(self, event):
        painter = QPainter(self)
        width, height = self.width(), self.height()
        cursor_pos = QCursor.pos()  # Get cursor position
        radius = 150  # Clear visibility radius around cursor
        
        # Dark overlay covering the screen
        painter.setBrush(Qt.black)
        painter.setPen(Qt.NoPen)
        painter.drawRect(0, 0, width, height)

        # Define the four corners
        corners = [(0, 0), (width, 0), (0, height), (width, height)]
        
        for corner_x, corner_y in corners:
            distance = ((cursor_pos.x() - corner_x) ** 2 + (cursor_pos.y() - corner_y) ** 2) ** 0.5
            if distance < 250:  # Activate clear zone when near corners
                corner_radius = max(50, min(200, distance))  # Dynamic radius
                
                gradient = QRadialGradient(cursor_pos.x(), cursor_pos.y(), corner_radius)
                gradient.setColorAt(0.0, Qt.transparent)
                gradient.setColorAt(1.0, Qt.black)
                
                painter.setBrush(QBrush(gradient))
                painter.drawRect(QRect(0, 0, width, height))  # Apply gradient effect
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrivacyFilter()
    window.show()
    sys.exit(app.exec())
