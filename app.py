from dotenv import load_dotenv
import streamlit as st

def main():
    load_dotenv()
    st.set_page_config(page_title = "Ask about your PDF")
    st.header("Ask about your PDF")

    pdf = st.file_uploader('Upload your PDF', type='pdf')

if __name__ == "__main__":
    main()