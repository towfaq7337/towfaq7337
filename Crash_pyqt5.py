#!/usr/bin/env python3
"""
Crash_pyqt5.py - مثال بسيط لواجهة PyQt5:
نافذة صغيرة مع زر ويعرض رسالة عند الضغط.
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox

class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crash.py - PyQt5 Demo")
        self.resize(300, 120)
        layout = QVBoxLayout()
        self.label = QLabel("مرحبًا — هذه نافذة تجريبية لـ PyQt5")
        btn = QPushButton("اضغطني")
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
