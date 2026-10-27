
import streamlit as st
from coding import analyze_text

st.title("Decentrathon Text Analyzer 🚀")

text = st.text_area("Enter your text:")

if st.button("Analyze"):
    if text:
        words, characters = analyze_text(text)

        st.success("Analysis completed!")
        st.write("Words:", words)
        st.write("Characters:", characters)
    else:
        st.warning("Please enter some text!")
