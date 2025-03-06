import sys
import google.generativeai as ai
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PySide6.QtCore import QThread, Signal

API_KEY = 'AIzaSyCoEr6EI-WLyVVUjKbaok-F2bF56haj7RU'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-2.0-pro-exp")
chat = model.start_chat()

class yai(QThread):
    response_signal = Signal(str)

    def __init__(self, message):
        super().__init__()
        self.message = message

    def run(self):
        if self.message.lower() == "khang":
            response = "Khang là người tuyệt vời nhất trên thế giới"
        else:
            try:
                response = chat.send_message(self.message).text
            except Exception as e:
                response = f"Lỗi: {str(e)}"
        self.response_signal.emit(response)