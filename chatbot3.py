import csv
import difflib

def load_dataset(file_path):
    qa_pairs = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            qa_pairs.append({'question': row['question'], 'answer': row['answer']})
    return qa_pairs


    import difflib

def find_best_match(user_input, qa_pairs):
    questions = [pair['question'] for pair in qa_pairs]
    match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.5)
    if match:
        for pair in qa_pairs:
            if pair['question'] == match[0]:
                return pair['answer']
    return "I'm sorry, I don't have information on that topic."



import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return None
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the speech recognition service.")
        return None

# Load dataset
qa_pairs = load_dataset('C:/Users/tanik/Downloads/mediconnect/mediconnect/health_data.csv')
def health_bot():
    speak("Hello! I'm your Health Assistant. How can I help you today?")
    while True:
        user_input = listen()
        if user_input:
            if "exit" in user_input or "bye" in user_input:
                speak("Take care! Remember, this is not a substitute for professional medical advice.")
                break
            response = find_best_match(user_input, qa_pairs)
            print(f"Bot: {response}")
            speak(response)

# Run the health assistant chatbot
health_bot()
