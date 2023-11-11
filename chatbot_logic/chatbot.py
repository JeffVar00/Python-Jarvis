
import json
from difflib import get_close_matches

def load_knowledge_base(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def save_knowledge_base(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def find_best_match(user_question, questions):
     matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
     return matches[0] if matches else None

def get_answer(user_question, knowledge_base):
    # check if the user's question is in the knowledge base
    for q in knowledge_base["questions"]:
        if q["question"] == user_question:
            return q["answer"]