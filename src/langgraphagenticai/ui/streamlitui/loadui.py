import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_title(page_title= "🤖" + self.config.get_page_title(), layout="wide")
        st.header("🤖" + self.config.get_page_title())

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_llm"] = st.select_box("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.confg.get_groq_model_options()