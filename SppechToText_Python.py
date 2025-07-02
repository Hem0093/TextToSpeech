# pip install SpeechRecognition 
# pip install pyaudio
import speech_recognition as sr
import os
import threading

from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

# Translate Hindi to English
def Translate_hindi_to_english(text):
    english_text = translate(text, "en-us")
    return english_text

# Convert speech to text
def Speech_To_Text_Python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + "Listening ..", end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.LIGHTBLACK_EX + "Recognizing......", end="", flush=True)
                recognizer_text = recognizer.recognize_google(audio).lower()
                if recognizer_text:
                    trans_text = Translate_hindi_to_english(recognizer_text)
                    print("\r" + Fore.BLUE + "Hemant : " + trans_text)
                    return trans_text
                else:
                    return ""
            except sr.UnknownValueError:
                print("\r" + Fore.RED + "Could not understand audio.", end="", flush=True)
            finally:
                print("\r", end="", flush=True)

    os.system("cls" if os.name == "nt" else "clear")

# Optional dummy print loop if needed
def print_loop():
    while True:
        pass

# Start threads
stt_thread = threading.Thread(target=Speech_To_Text_Python)
print_thread = threading.Thread(target=print_loop)

stt_thread.start()
print_thread.start()

stt_thread.join()
print_thread.join()



#Speech_To_Text_Python   

            
            
        
