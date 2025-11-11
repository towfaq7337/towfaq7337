#!/usr/bin/env python3
"""
Crash_pyqt5.py - مثال بسيط لواجهة PyQt5
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox

class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crash.py - PyQt5 Demo")
        self.resize(360, 140)
        layout = QVBoxLayout()
        self.label = QLabel("مرحبًا — مثال PyQt5 (Crash_pyqt5.py)")
        btn = QPushButton("اضغط هنا")
        btn.clicked.connect(self.on_click)
        layout.addWidget(self.label)
        layout.addWidget(btn)
        self.setLayout(layout)

    def on_click(self):
        QMessageBox.information(self, "تم", "تم الضغط على الزر! ✅")

def main():
    app = QApplication(sys.argv)
    win = DemoWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
