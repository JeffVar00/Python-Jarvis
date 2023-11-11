from speak_modules.speech_to_text import SpeechToText 
from chatbot_logic.openai_bot import send_to_chatbot
from chatbot_logic.chatbot import load_knowledge_base, find_best_match, get_answer, save_knowledge_base

def main_chatbot():

    knowledge_base = load_knowledge_base("chatbot_logic/knowledge_base/knowledge_base.json")
    print("Welcome to the chatbot, would you like to use text to speech or just text?")
    print("1. Voice Chat (English only)")
    print("2. Just text")
    choice = input("Enter your choice: ")

    if choice == '1':
        stt = SpeechToText()
        while True:
            print("Listening...")
            user_question= stt.record_audio()
            if user_question == "exit":
                break

            best_match = find_best_match(user_question, [q["question"] for q in knowledge_base["questions"]])
            if best_match:
                answer = get_answer(best_match, knowledge_base)
                stt.Speak(answer)
                print(f"Bot: {answer}")
            else:
                stt.Speak("I don't know the answer to that question. Teach me!")
                print("Bot: Sorry, I don't know the answer to that question. Teach me! Say your answer or say 'skip' to skip")
                print("Listening...")
                new_answer = stt.record_audio()

                if new_answer.lower() != 'skip':
                    knowledge_base["questions"].append({
                        "question": user_question,
                        "answer": new_answer
                    })
                    save_knowledge_base("chatbot_logic/knowledge_base/knowledge_base.json", knowledge_base)
                    stt.Speak("Thanks for teaching me!")

    elif choice == '2':
        
        while True:
            user_question = input("You: ")
            if user_question == "exit":
                break

            best_match = find_best_match(user_question, [q["question"] for q in knowledge_base["questions"]])
            if best_match:
                answer = get_answer(best_match, knowledge_base)
                print(f"Bot: {answer}")
            else:
                print("Bot: Sorry, I don't know the answer to that question. Teach me!")
                new_answer = input('Type your answer or "skip" to skip: ')

                if new_answer.lower() != 'skip':
                    knowledge_base["questions"].append({
                        "question": user_question,
                        "answer": new_answer
                    })
                    save_knowledge_base("chatbot_logic/knowledge_base/knowledge_base.json", knowledge_base)
                    print("Bot: Thanks for teaching me!")

def main_openai():

    # ask if the user wants to use text to speech or just text
    # if text to speech, initialize the text to speech class
    # if just text, initialize the chatbot class
    messages = [{'role': 'user', 'content': 'Please act like Jarvis from Iron Man'}]

    print("Welcome to the chatbot, would you like to use text to speech or just text?")
    print("1. Voice Chat (English only)")
    print("2. Just text")
    choice = input("Enter your choice: ")
    # if the user wants to use text to speech

    if choice == '1':
        # initialize the speech to text class
        stt = SpeechToText()
        while(1):
            # once this function runs what happens is that the python program waits from input from the user, waits for audio input from the user, and then it will return the audio input as a string
            text = stt.record_audio()

            if text == "exit":
                break

            # append the user's message to the messages list, the idea of the messages array is to keep track of the conversation
            messages.append({'role': 'user', 'content': text})
            print(f"You: {text}")

            # send the array to chatbot and get a response
            response = send_to_chatbot(messages)
            # append the chatbot's response to the text to speech function and play the response
            stt.Speak(response)
            # for accessibility purposes, print the response to the console
            print(f"Bot: {response}")

    # if the user wants to use just text
    elif choice == '2':
        while(1):
            text = input("You: ")
            if text == "exit":
                break
            messages.append({'role': 'user', 'content': text})
            response = send_to_chatbot(messages)
            print(f"Bot: {response}")

# main call

def main():
    response = input("Would you like to use the chatbot or the openai chatbot? (1 or 2): ")
    if response == '1':
        main_chatbot()
    elif response == '2':
        main_openai()

if __name__ == '__main__':
    main()
    