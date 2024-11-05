# Tech Chatbot Project

## Overview

This repository contains the code for a Tech Chatbot application that leverages multiple language models, including Google's Flan-T5 and GPT-2 from Hugging Face, to answer user questions and provide natural, interactive conversations. The project involves fine-tuning language models, integrating these models into a chatbot user interface, and deploying the system using Gradio for easy interaction. The aim is to create a sophisticated chatbot capable of handling a variety of user queries with accurate and meaningful responses.

The main components of this project include:
- A Flan-T5 based chatbot using PyQt5 for UI (`google_flan_t5.py`), which allows the chatbot to generate high-quality responses.
- A GPT-2 based chatbot with a user-friendly interface (`Hugginface_gpt2.py`) for a different approach to conversational AI, offering more flexibility in response generation.
- An LLM fine-tuning notebook demonstrating step-by-step training procedures (`llm-finetuning.ipynb`) to enhance the performance of language models for specific use cases.
- A UI implementation using PyQt5 for the chatbot interface (`UI.py`), which provides an intuitive and colorful interface to interact with the chatbot seamlessly.

This project is designed to leverage the state-of-the-art capabilities of these language models and to make advanced natural language processing accessible and interactive for users through a convenient UI.

## Project Structure

- `google_flan_t5.py`:
  - Contains the implementation for using Google's Flan-T5 model to generate responses.
  - Uses PyQt5 to create a graphical user interface for the chatbot, making it easy for users to interact.
  - Loads the Flan-T5 model and tokenizer from the Hugging Face Transformers library, providing efficient language understanding and generation capabilities.

- `Hugginface_gpt2.py`:
  - Implements a chatbot using a fine-tuned GPT-2 model for conversational responses.
  - Provides an interactive UI for asking questions and getting answers using PyQt5, making the interaction experience user-friendly.
  - Loads a local GPT-2 model checkpoint for question-answering purposes, allowing the chatbot to generate relevant and meaningful responses.

- `llm-finetuning.ipynb`:
  - Jupyter notebook that demonstrates the steps for fine-tuning a large language model (LLM) on custom datasets.
  - Uses the Hugging Face library for model training and evaluation, helping improve model performance for specific tasks.
  - Designed to run on a Kaggle environment with GPU support for accelerated training, allowing for faster experimentation and model tuning.

- `UI.py`:
  - Implements the user interface for the chatbot using PyQt5.
  - Provides a colorful and intuitive chat interface that allows users to interact with the language model easily.
  - Designed to be straightforward and user-friendly, enabling users of any technical background to engage with the chatbot effectively.

## Features
- **Model Integration**: Uses state-of-the-art LLMs like Flan-T5 and GPT-2 from Hugging Face, allowing for advanced language comprehension and generation.
- **Interactive UI**: Built with PyQt5 to provide an easy and interactive user experience, making it accessible to users without programming knowledge.
- **Fine-tuning Notebook**: Demonstrates how to fine-tune an LLM on a dataset to improve chatbot response accuracy, enabling customization for specific use cases.
- **Deployment**: The chatbot can be deployed using Gradio for ease of access on web browsers, allowing users to interact with the chatbot from anywhere without needing to install additional software.

## Requirements

To run this project locally, you need the following dependencies:

- Python 3.8+
- PyQt5
- Transformers (Hugging Face)
- PyTorch
- Gradio (for web-based deployment)
- Jupyter Notebook (for viewing/editing `llm-finetuning.ipynb`)

You can install the dependencies using:

```sh
pip install -r requirements.txt
```

> Note: Ensure that you have a GPU-enabled environment for training the models, especially for fine-tuning, as it significantly speeds up the training process and allows for better performance.

## Getting Started

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Musawer1214/tech-chatbot.git
   cd tech-chatbot
   ```

2. **Install Dependencies**:
   Install all required Python packages.
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the UI**:
   - To run the Flan-T5 chatbot UI, execute:
     ```sh
     python google_flan_t5.py
     ```
   - To run the GPT-2 chatbot UI, execute:
     ```sh
     python Hugginface_gpt2.py
     ```

4. **Fine-tune a Model**:
   - Open `llm-finetuning.ipynb` in Jupyter Notebook.
   - Follow the steps to fine-tune a language model with your dataset, allowing the chatbot to better understand specific domain-related queries and provide more relevant responses.

5. **Deploy the Chatbot**:
   - Use Gradio for deployment.
   - Example:
     ```sh
     python deploy_gradio.py
     ```
   - Gradio provides an easy and accessible way to share the chatbot, even for users who do not have the technical expertise to run the code locally.

## Usage
- **Flan-T5 Chatbot**: Provides answers to user questions using Google's Flan-T5 model, known for its natural and context-aware responses.
- **GPT-2 Chatbot**: Uses a fine-tuned GPT-2 model to generate responses, which allows for a conversational experience that feels dynamic and engaging.
- **Interactive UI**: The UI is built using PyQt5, providing a simple and effective way to interact with the chatbot. The design aims to be clean and intuitive, making it accessible to a wide range of users.

## Screenshots
- Add screenshots here to demonstrate the UI and deployment process. Screenshots can help new users understand what to expect and guide them in using the chatbot effectively.

## Future Work
- Implement additional model architectures for more diverse response generation, including multilingual support to cater to a wider audience.
- Integrate with cloud services for scalable deployment, such as AWS or Google Cloud, to ensure that the chatbot can handle increased traffic and provide consistent performance.
- Add support for voice-based interaction, allowing users to speak directly to the chatbot for a more natural conversational experience.
- Enhance the UI with additional features such as saving conversation history and providing more customization options for users.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements. Whether it's adding new features, improving existing functionality, or fixing bugs, all contributions are appreciated. Be sure to follow the coding standards outlined in the repository and add detailed comments to help maintain the readability of the code.

## License
This project is licensed under the MIT License - see the LICENSE file for details. The MIT License allows you to freely use, modify, and distribute the code, making it suitable for both personal and commercial use.

## Acknowledgments
- Hugging Face for providing pre-trained models and the Transformers library, which greatly simplifies the process of working with LLMs.
- PyQt5 for UI components that help create a visually appealing and interactive interface.
- Kaggle for providing GPU resources for model fine-tuning, making the training process faster and more efficient.
- The open-source community for continuously supporting and improving the tools that make projects like this possible.

---

Feel free to reach out for any questions or suggestions! This project is continuously evolving, and your feedback is valuable in helping improve the chatbot and add new features that make it even more useful and accessible.
