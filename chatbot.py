from speak_modules.speech_to_text import SpeechToText 

def main():

    # initialize the speech to text class
    stt = SpeechToText()
    
    messages = [{'role': 'user', 'content': 'Please act like Jarvis from Iron Man'}]
    while(1):
        # once this function runs what happens is that the python program waits from input from the user, waits for audio input from the user, and then it will return the audio input as a string
        text = stt.record_audio()
    
        # append the user's message to the messages list, the idea of the messages array is to keep track of the conversation
        messages.append({'role': 'user', 'content': text})
        print(text)

        # send the array to chatbot and get a response
        response = stt.send_to_chatbot(messages)

        # append the chatbot's response to the text to speech function and play the response
        stt.Speak(response)

        # for accessibility purposes, print the response to the console
        print(response)

# main call
if __name__ == '__main__':
    main()