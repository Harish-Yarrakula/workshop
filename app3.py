from google import genai 
from dotenv import load_dotenv
import os 
import streamlit as st

load_dotenv()
models=["gemini-3.5-flash","gemini-3.5-flash-lite","gemini-3.6-flash","gemini-3.6-flash-lite"]
with st.sidebar:
    st.subheader("Model Info")
    model=st.selectbox("Select a model: ",models)
client=genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
st.set_page_config(page_title="AI Translator",layout="wide")
st.title("AI Translator")
st.caption("Powered by Gemini 3.6 Flash")

lang=["Telugu","Hindi","Kannada","Tamil","Spanish","French","Chinese","Japenese","German","English",""]

if "source_language" not in st.session_state:
    st.session_state.source_language="English"
if "destination_language" not in st.session_state:
    st.session_state.destination_language="Telugu"
col1,col2=st.columns(2)
with col1:
    source_language=st.selectbox(
        "Source",
        lang,
        index=lang.index(
            st.session_state.source_language
        )
    )
with col2:
    destination_language=st.selectbox(
        "Destination",
        lang,
        index=lang.index(
           st.session_state.destination_language 
        )
    )
st.session_state.source_lagnuage=source_language
st.session_state.destination_language=destination_language
if st.button("swap"):
    st.session_state.source_language,st.session_state.destination_language=st.session_state.destination_language,st.session_state.source_language

text=st.text_area("Enter text to translate: ")

if st.button("Translate"):
    prompt=f"""
    Translate {text} from {source_language} to {destination_language}
    strict rules:
    1. dont add extra info
    2. dont remove existing info
    3. dont summarise the {text}
    4. act as professonal native translator
    5. give me response like in native language of {destination_language}
    """

    if prompt:
        res=client.models.generate_content(
            model=model,
            contents=prompt
        )
        st.subheader("TRANSLATION: ")
        st.text_area("Translated text is :",res.text)
