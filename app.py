import streamlit as st
# Function to open the URL in a new tab
import webbrowser
def open_url(url):
    webbrowser.open_new_tab(url)

st.set_page_config(
    page_title="Rava Bookmarks",
    page_icon="🔖"
)
st.title("Rava.AI")

# Define the URLs
url1 = "https://dynamic-prompt-generator.streamlit.app/"
url2 = "https://static-workflows.streamlit.app/"
url3 = "https://strategy-module.streamlit.app/"

# Create buttons for each URL
if st.button("Dynamic Prompt Generator🚀"):
    open_url(url1)

if st.button("Static Workflows🔄"):
    open_url(url2)

if st.button("Strategy Module♞"):
    open_url(url3)