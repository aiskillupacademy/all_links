import streamlit as st

st.set_page_config(
    page_title="Rava Bookmarks",
    page_icon="🔖"
)
st.title("Rava.AI")

# Define the URLs
url1 = "https://dynamic-prompt-generator.streamlit.app/"
url2 = "https://static-workflows.streamlit.app/"
url3 = "https://strategy-module.streamlit.app/"
url4 = "https://brand-voice-promptgen.streamlit.app/"
url5 = "https://blog-builder.streamlit.app/"
url6 = "https://linkedin-enrich.streamlit.app/"
url7 = "https://querychatbot.streamlit.app/"

# Create hyperlinks using markdown
st.header("Subhraneel")
st.markdown(f"[Dynamic Prompt Generator🚀]({url1})")
st.markdown(f"[Static Workflows🔄]({url2})")
st.markdown(f"[Strategy Module♞]({url3})")
st.markdown(f"[Brand Voice Prompt Generator🎙️]({url4})")
st.markdown(f"[Blog Builder📝]({url5})")
st.markdown(f"[Lead/Contact Enrichment from LinkedIn Profile ✨]({url6})")

st.header("Subham")
st.markdown(f"[ChatBot]({url7})")