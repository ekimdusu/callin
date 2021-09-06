import streamlit as st
import speech_recognition as sr
from gtts import gTTS 
from os import path
import pydub as AudioSegment
from googletrans import Translator
import sounddevice as sd
from scipy.io.wavfile import write
import os

st.sidebar.title("ML çeviri denemeleri")
menu = st.sidebar.radio("Ne yapmak istersiniz?", ("Yazıyı sese çeviri", "Yazıyı İngilizce sese çevir", "Sesi yazıya çevir", "Sesi İngilizce yazıya çevir"))
if menu == 'Yazıyı sese çeviri':
    input = st.text_input("Ne söylememi istersin?")
    if input != "":
        tts = gTTS(text=input, lang='tr', slow=False)
        file = "/app/callin/output.mp3"
        tts.save(file)
        audioFile = open(file, 'rb')
        audioBytes = audioFile.read()
        st.audio(audioBytes, format='audio/ogg',start_time=0)
elif menu == 'Yazıyı İngilizce sese çevir':
    input = st.text_input("Ne söylememi istersin?")
    if input != "":
        translator = Translator()
        translate_text = translator.translate(input, dest='en').text
        tts = gTTS(text=translate_text, lang='en', slow=False)
        file = "/app/callin/output.mp3"
        tts.save(file)
        audioFile = open(file, 'rb')
        audioBytes = audioFile.read()
        st.audio(audioBytes, format='audio/ogg',start_time=0)
elif menu == 'Sesi İngilizce yazıya çevir':
    r = sr.Recognizer()
    #st.write(sd.query_devices())
    fs = 44100 
    seconds = 5
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  
    write('/app/callin/output.wav', fs, myrecording) 

    with sr.AudioFile('/app/callin/output.wav') as source:
        audio = r.listen(source)  
    try:
        text = r.recognize_google(audio, language="tr-tr")
        translator = Translator()
        translate_text = translator.translate(input, dest='en').text
        st.write(translate_text)
    except sr.UnknownValueError:
        st.write("Söylediğini anlamadım")
