import streamlit as st
import speech_recognition as sr
from gtts import gTTS 
from os import path
import pydub as AudioSegment
import google_trans_new from google_translator  
#import sounddevice as sd
from scipy.io.wavfile import write

st.sidebar.title("ML çeviri denemeleri")
menu = st.sidebar.radio("Ne yapmak istersiniz?", ("Yazıyı sese çeviri", "Yazıyı İngilizce sese çevir", "Sesi yazıya çeviri", "Sesi İngilizce yazıya çevir"))
if menu == 'Yazıyı sese çeviri':
    input = st.text_input("Ne söylememi istersin?")
    if input != "":
        tts = gTTS(text=input, lang='tr', slow=False)
        tts.save("output.mp3")
        audioFile = open('output.mp3', 'rb')
        audioBytes = audioFile.read()
        st.audio(audioBytes, format='audio/ogg',start_time=0)
elif menu == 'Yazıyı İngilizce sese çevir':
    input = st.text_input("Ne söylememi istersin?")
    if input != "":
        translator = google_translator()  
        translate_text = translator.translate(input, lang_tgt='en')  
        tts = gTTS(text=translate_text, lang='en', slow=False)
        tts.save("output.mp3")
        audioFile = open('output.mp3', 'rb')
        audioBytes = audioFile.read()
        st.audio(audioBytes, format='audio/ogg',start_time=0)
