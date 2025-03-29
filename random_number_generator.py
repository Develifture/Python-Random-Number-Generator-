import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton

class RandomNumberGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Number Generator")
        self.setGeometry(100, 100, 300, 250)
        self.dark_mode = False
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Create label
        self.number_label = QLabel("Click the button to generate a number", self)
        self.number_label.setStyleSheet("font-size: 32px;")
        self.number_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.number_label)
        
        # Create buttons
        self.generate_button = QPushButton("Generate Random Number", self)
        self.generate_button.clicked.connect(self.generate_random_number)
        layout.addWidget(self.generate_button)
        
        self.theme_button = QPushButton("Toggle Dark Mode", self)
        self.theme_button.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_button)
        
        # Set initial theme and generate number
        self.set_theme()
        self.generate_random_number()
    
    def set_theme(self):
        if self.dark_mode:
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #333;
                }
                QLabel {
                    color: white;
                }
                QPushButton {
                    background-color: #555;
                    color: white;
                    border: 1px solid #777;
                    padding: 10px;
                    font-size: 32px;
                }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #f0f0f0;
                }
                QLabel {
                    color: black;
                }
                QPushButton {
                    background-color: #e0e0e0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 10px;
                    font-size: 32px;
                }
            """)
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()
    
    def generate_random_number(self):
        random_num = random.randint(1, 1000)
        self.number_label.setText(f"Random Number: {random_num}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RandomNumberGenerator()
    window.show()
    sys.exit(app.exec_())