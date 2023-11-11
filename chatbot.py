from speak_modules.speech_to_text import SpeechToText 
from chatbot_logic.openai import send_to_chatbot

def main():

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
            # append the user's message to the messages list, the idea of the messages array is to keep track of the conversation
            messages.append({'role': 'user', 'content': text})
            print(text)
            # send the array to chatbot and get a response
            response = send_to_chatbot(messages)
            # append the chatbot's response to the text to speech function and play the response
            stt.Speak(response)
            # for accessibility purposes, print the response to the console
            print(response)

    # if the user wants to use just text
    elif choice == '2':
        while(1):
            text = input("Enter your message: ")
            messages.append({'role': 'user', 'content': text})

            response = send_to_chatbot(messages)
            print(response)

# main call
if __name__ == '__main__':
    main()