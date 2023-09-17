import streamlit as st
from googletrans import LANGUAGES, Translator
from gtts import gTTS
import os
import speech_recognition as sr
import pyaudio
import playsound

# Function to recognize speech input
def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
    return translated_text

def translate_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = r.listen(source, phrase_time_limit=10)
        st.write("Processing...")
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand your speech.")
        return None
    except sr.RequestError:
        st.write("Sorry, I am unable to process your request at the moment.")
        return None

def play_audio(audio):
    playsound.playsound(audio)

def main():
    st.subheader("Language Translator")
    st.sidebar.write("S. Tauqir Ahmed - BV of DSAI")
    st.sidebar.write("Mentors: Sir Qasim")
    st.sidebar.image("nedpic.jpg")
    
    input_lang = st.selectbox("Select Input Language", list(LANGUAGES.values()))
    output_lang = st.selectbox("Select Output Language", list(LANGUAGES.values()))
    
    input_type = st.radio("Select Input Type", ("Speech", "Text"))
    output_type = st.radio("Select Output Type", ("Text", "Speech"))
    
    if input_type == "Speech":
        if st.button("Translate"):
            text = translate_speech()
            if text:
                translated_text = translate_text(text, input_lang, output_lang)
                st.write("Translated Output:")
                if output_type == "Text":
                    st.write(translated_text)
                else:
                    tts = gTTS(text=translated_text, lang=output_lang)
                    tts.save("output.mp3")
                    play_audio("output.mp3")
    else:
        text = st.text_input("Enter Text")
        if st.button("Translate"):
            translated_text = translate_text(text, input_lang, output_lang)
            st.write("Translated Output:")
            if output_type == "Text":
                st.write(translated_text)
            else:
                tts = gTTS(text=translated_text, lang=output_lang)
                tts.save("output.mp3")
                play_audio("output.mp3")

if __name__ == "__main__":
    main()