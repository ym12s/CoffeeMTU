import sys
import google.generativeai as ai
import time
import random
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PySide6.QtCore import QThread, Signal, QTimer

API_KEY = 'AIzaSyCoEr6EI-WLyVVUjKbaok-F2bF56haj7RU'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

import time
from PySide6.QtCore import QThread, Signal

class yai(QThread):
    response_signal = Signal(str)

    def __init__(self, message):
        super().__init__()
        self.message = message
    def run(self):
        try:
            response = chat.send_message(self.message).text
        except Exception as e:
            response = f"Lỗi: {str(e)}"
        updated_response = self.process_ai_response(response)
        # for char in updated_response:
        #     response_text += char
        #     if char != '\n' and char != '**': 
        #     time.sleep(0.03)  
        self.response_signal.emit(updated_response)

    def process_ai_response(self, response):
        # Thay thế từ "Google" bằng "Trần Công Khang"
        return response.replace("Google", "Trần Công Khang")

    
    
    