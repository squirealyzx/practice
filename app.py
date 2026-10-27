
import streamlit as st

st.title("AI Text Analyzer 🚀")

text = st.text_area("Enter your text:")

if st.button("Analyze"):
    if text:
        words = text.split()

        st.success("Analysis completed!")
        st.write("Words:", len(words))
        st.write("Characters:", len(text))
    else:
        st.warning("Please enter some text!")


