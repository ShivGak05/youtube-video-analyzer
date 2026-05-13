import streamlit as st
from video_agent import agent
import pandas as pd
st.set_page_config(
    page_title="Agentic AI Demo",
    page_icon="🤖",
    layout="centered",
)
st.title("AI youtube video agent")

@st.cache_resource
def get_agent():
    return agent
agent=get_agent()

video_url=st.text_input("Enter youtube video link:")
button=st.button("Analyze video")
if video_url and button:
    with st.spinner("Analyzing video..."):
        response=agent.run(
            f"Analyze this video: {video_url}"
        )
    st.markdown(response.content)
