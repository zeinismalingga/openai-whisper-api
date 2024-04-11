from openai import OpenAI
import streamlit as st

st.title("OpenAI Transcribe Audio")

# add sidebar
with st.sidebar:
    api_key = st.text_input("Enter your OpenAI API key", type="password")


# add audio file uploader
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

# transcribe audio
if uploaded_file is not None and api_key is not None:
    with st.spinner("Transcribing audio..."):
        client = OpenAI(api_key=api_key)

        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=uploaded_file
        )

        st.info(transcription)
