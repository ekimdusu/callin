import streamlit as st
import speech_recognition as sr
from gtts import gTTS 
from os import path
import pydub as AudioSegment
from googletrans import Translator
#import sounddevice as sd
from scipy.io.wavfile import write
import playsound
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
elif menu == 'Sesi yazıya çevir':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Birşeyler Söyle!")
        audio = r.listen(source)
    #st.write(sd.query_devices())
    data = ""
    try:
        data = r.recognize_google(audio, language='tr-tr')
        data = data.lower()
        st.write("Bunu Söyledin :" + data)
    except sr.UnknownValueError:
        st.write("Ne dediğini anlamadım")
