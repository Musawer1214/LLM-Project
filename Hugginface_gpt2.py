from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QLabel, QScrollArea)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import sys

# Load the fine-tuned QA model and tokenizer
model_path = "fine_tuned_model"  # Path to the model directory (replace if different)
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForQuestionAnswering.from_pretrained(model_path)

# Set up the question-answering pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Define a context for the chatbot to use
# You can expand this or make it more dynamic if necessary
context = """
Zamu AI is a remote-based company located in Peshawar, Pakistan. The company provides AI-related solutions, 
including data gathering, model training, large language model (LLM) services, and LangChain solutions. 
Zamu AI assists businesses looking to implement AI solutions in various fields, such as healthcare, finance, and retail.
"""

class ColorfulChatWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set up main window properties
        self.setWindowTitle("Tech Chatbot")
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

        # Display user message with vibrant color
        user_label = QLabel(f"You: {user_text}")
        user_label.setFont(QFont("Arial", 12))
        user_label.setStyleSheet("background-color: #8e44ad; color: white; padding: 10px; border-radius: 15px;")
        user_label.setAlignment(Qt.AlignRight)
        self.chat_container_layout.addWidget(user_label)

        # Use QA pipeline to get the answer based on the context and user question
        response = qa_pipeline(question=user_text, context=context)
        answer = response["answer"]

        # Display bot response
        bot_label = QLabel(f"Chatbot: {answer}")
        bot_label.setFont(QFont("Arial", 12))
        bot_label.setStyleSheet("background-color: #3498db; color: white; padding: 10px; border-radius: 15px;")
        bot_label.setAlignment(Qt.AlignLeft)
        self.chat_container_layout.addWidget(bot_label)

        # Clear input field and scroll to bottom
        self.input_field.clear()
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

# Run the application
app = QApplication(sys.argv)
window = ColorfulChatWidget()
window.show()
sys.exit(app.exec_())
