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
menu = st.sidebar.radio("Ne yapmak istersiniz?", ("Yazıyı sese çeviri", "Yazıyı İngilizce sese çevir", "Sesi yazıya çeviri", "Sesi İngilizce yazıya çevir"))
if menu == 'Yazıyı sese çeviri':
    input = st.text_input("Ne söylememi istersin?")
    if input != "":
        tts = gTTS(text=input, lang='tr', slow=False)
        file = "/app/callin/output.mp3"
        tts.save(file)
        playsound.playsound(file, True)
elif menu == 'Yazıyı İngilizce sese çevir':
    input = st.text_input("Ne söylememi istersin?")
    if input != "":
        translator = Translator()
        translate_text = translator.translate(input, dest='en').text
        tts = gTTS(text=translate_text, lang='en', slow=False)
        file = "/app/callin/output.mp3"
        tts.save(file)
        playsound.playsound(file, True)
