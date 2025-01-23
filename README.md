# End-to-End-Medical-Chatbot
Medical Chatbot
Welcome to the Medical Chatbot project! This repository contains an end-to-end medical chatbot designed to assist users by providing information on medical conditions based on user-input symptoms. The chatbot leverages advanced natural language processing (NLP) techniques to deliver accurate and helpful responses.

Table of Contents
Features
Technologies Used
Installation
Usage
Project Structure
License
Features
Symptom Analysis: Users can input symptoms, and the chatbot will analyze them to suggest possible medical conditions.
Interactive Conversations: The chatbot engages in a conversational manner, asking follow-up questions to gather more information when necessary.
Medical Information: Provides details about diseases, their symptoms, causes, treatments, and preventive measures.
Technologies Used
Programming Languages:
Python
HTML
CSS
Frameworks and Libraries:
Flask: A lightweight WSGI web application framework in Python.
Transformers: Provides general-purpose architectures for natural language understanding and generation.
Sentence Transformers: Enables easy and efficient computation of dense vector representations for sentences.
LangChain: Facilitates the development of applications powered by language models.
Pinecone Client: Interfaces with Pinecone, a vector database for machine learning applications.
LangChain-Pinecone: Integrates LangChain with Pinecone for enhanced vector storage capabilities.
PyPDF: A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files.
LangChain-Community: Contains community-contributed LangChain integrations.
Python-dotenv: Reads key-value pairs from a .env file and can set them as environment variables.
Installation
To set up the project locally, follow these steps:

Clone the repository:

bash

git clone https://github.com/UniteUniverse/Medical-Chatbot.git
cd Medical-Chatbot
Create a virtual environment:

bash

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

bash

pip install -r requirements.txt
Set up environment variables:

Create a .env file in the project root directory and add the necessary environment variables, such as API keys and configuration settings.

Usage
Start the application:

bash

python app.py
Access the chatbot:

Open your web browser and navigate to http://localhost:5000/.

Interact with the chatbot:

Enter your symptoms or medical queries in the chat interface.
The chatbot will respond with possible conditions and may ask follow-up questions for clarification.
Continue the conversation to receive more detailed information.
Project Structure
app.py: The main application file that runs the Flask server.
templates/: Contains HTML templates for the web pages.
static/: Contains static files like CSS and JavaScript.
models/: Includes machine learning models used for symptom analysis.
data/: Contains datasets used for training and reference.
src/: Source code for various components of the chatbot.
requirements.txt: Lists all the Python dependencies required for the project.
.env: Environment variables file containing configuration settings.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Note: This chatbot is intended for informational purposes only and is not a substitute for professional medical advice. Always consult with a qualified healthcare provider for medical concerns.
