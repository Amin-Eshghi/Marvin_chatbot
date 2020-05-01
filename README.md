# Marvin_chatbot
Developing Conversational AI on top of RASA



**Step 1: Use Python 3.6**
- conda create -n rasa python=3.6
- conda activate rasa

**Step 2: Install the requirements**
- pip install -r requirements.txt

**Step 3: Install the spaCy English language model by running**
- python -m spacy download en

**Step 4: Train the NLU model**
- make train-nlu

**Step 5: Train the Core model**
- make train-core

**Step 6: Start the conversation**
- make cmdline
