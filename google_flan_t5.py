from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QScrollArea)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
import sys

# Load the Flan-T5 model and tokenizer
model_name = "google/flan-t5-large"  # You can try "google/flan-t5-xl" for even better performance
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Function to generate responses
def generate_response(input_text):
    # Encode the input
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate response with Flan-T5
    outputs = model.generate(
        input_ids,
        max_length=100,
        temperature=0.7,    # Increase temperature for more randomness
        top_p=0.9,          # Use nucleus sampling for diversity
        repetition_penalty=1.5,  # Penalize repetition
        num_return_sequences=1
    )

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

class ChatbotWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main window properties
        self.setWindowTitle("Chatbot")
        self.setFixedSize(400, 600)
        self.setStyleSheet("background-color: #f0f8ff;")  # Light blue background

        # Main layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Scroll Area for chat history
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.chat_container = QWidget()
        self.chat_container_layout = QVBoxLayout()
        self.chat_container.setLayout(self.chat_container_layout)
        self.scroll_area.setWidget(self.chat_container)
        layout.addWidget(self.scroll_area)

        # Input field layout
        self.input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type a message...")
        self.input_field.setFont(QFont("Arial", 12))
        self.input_field.setStyleSheet("border: 1px solid #ccc; padding: 8px; border-radius: 10px;")

        self.send_button = QPushButton("Send")
        self.send_button.setFont(QFont("Arial", 12))
        self.send_button.setStyleSheet("background-color: #00bcd4; color: white; padding: 8px; border-radius: 10px;")
        self.send_button.clicked.connect(self.send_message)

        self.input_layout.addWidget(self.input_field)
        self.input_layout.addWidget(self.send_button)
        layout.addLayout(self.input_layout)

    def send_message(self):
        user_text = self.input_field.text()
        if user_text.strip() == "":
            return

        # Display user message
        user_label = QLabel(f"You: {user_text}")
        user_label.setFont(QFont("Arial", 12))
        user_label.setStyleSheet("background-color: #8e44ad; color: white; padding: 10px; border-radius: 15px;")
        user_label.setAlignment(Qt.AlignRight)
        self.chat_container_layout.addWidget(user_label)

        # Generate response from Flan-T5
        response = generate_response(f"Answer the question: {user_text}")

        # Display bot response
        bot_label = QLabel(f"Chatbot: {response}")
        bot_label.setFont(QFont("Arial", 12))
        bot_label.setStyleSheet("background-color: #3498db; color: white; padding: 10px; border-radius: 15px;")
        bot_label.setAlignment(Qt.AlignLeft)
        self.chat_container_layout.addWidget(bot_label)

        # Clear input field and scroll to bottom
        self.input_field.clear()
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

# Run the application
app = QApplication(sys.argv)
window = ChatbotWidget()
window.show()
sys.exit(app.exec_())
