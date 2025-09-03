# AI Agent For Web3 Disputes Transactions

## Description
This project implements an AI agent designed to assist in managing and resolving disputes related to Web3 transactions. The agent utilizes machine learning models to provide responses to user inquiries based on a predefined FAQ dataset.


![megatron](https://github.com/user-attachments/assets/082d8c47-702f-49fe-8d69-1e16b0fec9af)

## Key Components
- **`src/main.py`:** The main entry point for the chatbot. It initializes the FAQ model and handles user interactions.
- **`src/train.py`:** Script for training the FAQ models using DeepPavlov. It trains two models: one with FastText logistic regression and another with TF-IDF auto FAQ.
- **`src/config.json`:** Configuration file that defines the models and their training parameters, including the data source.
- **`data/faq_data.json`:** Contains the frequently asked questions and their corresponding answers used for training the models.
- **`requirements.txt`:** Lists the necessary Python packages required to run the project.
- **`.gitignore`:** Specifies files and directories to be ignored by Git.

.=#.

## Installations
1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd AI-Agent-For-Web3-Disputes-Transactions
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Train the models:
   ```bash
   python src/train.py
   ```

2. Run the chatbot:
   ```bash
   python src/main.py
   ```

3. Interact with all the chatbot by typing your questions. Type 'exit' or 'quit' to end the session.
