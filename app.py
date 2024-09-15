import streamlit as st
import openai
from PyPDF2 import PdfReader
import os
import tiktoken

def extract_text_from_pdf(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def num_tokens_from_string(string: str, model: str = "gpt-4") -> int:
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def split_text_by_sections(text):
    # Split the resume into sections based on headings or double newlines
    sections = text.split('\n\n')
    return [section.strip() for section in sections if section.strip() != ""]

st.title("LinkedIn PDF to HTML Resume Converter")

api_key = st.text_input("Enter your OpenAI API Key:", type="password")

uploaded_file = st.file_uploader("Upload your LinkedIn PDF resume", type=["pdf"])

if uploaded_file and api_key:
    with st.spinner("Processing..."):
        try:
            resume_text = extract_text_from_pdf(uploaded_file)
            if not resume_text.strip():
                st.error("No text could be extracted from the uploaded PDF.")
            else:
                sections = split_text_by_sections(resume_text)
                html_resume = "<html><head><meta charset='UTF-8'><title>Resume</title></head><body>"

                for idx, section in enumerate(sections):
                    prompt = f"""Convert the following section of a resume into a structured HTML format. Use appropriate HTML tags like <h1>, <h2>, <p>, <ul>, <li>, etc. Ensure the output is well-formatted and valid HTML.

Section Text:
{section}
"""
                    prompt_tokens = num_tokens_from_string(prompt, model="gpt-4")
                    max_context_tokens = 8192
                    # Reserve tokens for the response
                    max_completion_tokens = min(max_context_tokens - prompt_tokens, 2000)

                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=max_completion_tokens,
                        temperature=0.5
                    )

                    html_section = response.choices[0].message.content
                    finish_reason = response.choices[0].finish_reason

                    if finish_reason == 'length':
                        st.warning(f"The generated output for section {idx+1} was cut off due to token limit.")

                    html_resume += html_section

                html_resume += "</body></html>"

                st.success("Conversion Successful!")
                st.markdown("### HTML Resume")
                st.components.v1.html(html_resume, height=800, scrolling=True)
                st.download_button(
                    label="Download HTML Resume",
                    data=html_resume,
                    file_name="resume.html",
                    mime="text/html"
                )
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
elif uploaded_file:
    st.warning("Please enter your OpenAI API Key.")
