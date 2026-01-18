import time
import streamlit as st
from scraper import extract_main_content
from summarizer import summarize_text

RATE_LIMIT_SECONDS = 30

st.set_page_config(
    page_title="Web Page Summarizer",
    page_icon="🌐",
    layout="centered"
)

st.markdown(
    """
    <style>
        /* Peacock Green button (Primary button) */
    div.stButton > button[kind="primary"] {
        background-color: #006D5B !important;
        color: white !important;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #00897B !important;
    }

    /* Blue Download Button */
    div.stDownloadButton > button {
        background-color: #1E88E5 !important;
        color: white !important;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
    }

    div.stDownloadButton > button:hover {
        background-color: #1565C0 !important;
    }

    /* Hide 'Press Enter to apply' text under input boxes */
    div[data-testid="InputInstructions"] {
        display: none;
    }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

if "last_request_time" not in st.session_state:
    st.session_state.last_request_time = 0

if "summary" not in st.session_state:
    st.session_state.summary = None

st.title("🌐 Web Page Summarizer")
st.caption("AI-powered structured summaries")

st.divider()

url = st.text_input(
    "Enter a website URL",
    placeholder="https://en.wikipedia.org/wiki/Air_India"
)
st.caption("👉 After entering the URL, click **Generate Summary** to proceed.")


if st.button("Generate Summary", type="primary"):
    now = time.time()
    elapsed = now - st.session_state.last_request_time

    if elapsed < RATE_LIMIT_SECONDS:
        st.warning(
            f"⏳ Please wait {int(RATE_LIMIT_SECONDS - elapsed)} seconds."
        )
    elif not url:
        st.warning("Please enter a valid URL.")
    else:
        try:
            st.session_state.last_request_time = now

            with st.spinner("🔍 Extracting content..."):
                content = extract_main_content(url)

            with st.spinner("🧠 Generating summary..."):
                st.session_state.summary = summarize_text(content)

            st.success("Summary generated successfully!")

        except Exception as e:
            st.error(f"Error: {e}")

if st.session_state.summary:
    st.divider()
    st.markdown(st.session_state.summary)

    st.download_button(
        "Download Summary",
        st.session_state.summary,
        file_name="summary.md"
    )

st.divider()
st.caption("© Web Page Summarizer - By Parth Joshi")
