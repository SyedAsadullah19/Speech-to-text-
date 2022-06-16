import speech_recognition as sr
import urllib.request as ul
url= str(input("Paste the file here:"))
url_r=ul.urlopen(url)
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(url_r) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_sphinx(audio_data)
    print(text)
