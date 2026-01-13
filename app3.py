import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

st.set_page_config(page_title="AI Study Buddy", layout="wide")

# Title
st.title("📚 AI Powered Study Buddy")
st.write("Explain topics, summarize notes, generate quizzes & flashcards instantly!")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(
    ["Explain Topic", "Summarize Notes", "Quiz Generator", "Flashcards"]
)

# -------------------- TAB 1: Explain Topic --------------------
with tab1:
    st.header("Explain Any Topic")
    topic = st.text_input("Enter the topic you want explained:")

    if st.button("Explain"):
        if topic.strip() == "":
            st.warning("Please enter a topic!")
        else:
            with st.spinner("Explaining..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=f"Explain the topic '{topic}' in a simple and clear way for a student."
                )

            st.success("Explanation Ready!")
            st.markdown(f"### 🔍 Explanation for **{topic}**")
            st.write(response.output_text)

# -------------------- TAB 2: Summarize Notes --------------------
with tab2:
    st.header("Summarize Notes")
    notes = st.text_area("Paste your notes here:")

    if st.button("Summarize"):
        if notes.strip() == "":
            st.warning("Please paste some notes!")
        else:
            with st.spinner("Summarizing..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=f"Summarize the following notes into clear bullet points:\n\n{notes}"
                )

            st.success("Summary Ready!")
            st.write(response.output_text)

# -------------------- TAB 3: Quiz Generator --------------------
with tab3:
    st.header("Quiz Generator")
    quiz_topic = st.text_input("Enter topic for quiz:")

    if st.button("Generate Quiz"):
        if quiz_topic.strip() == "":
            st.warning("Please enter a topic!")
        else:
            with st.spinner("Creating quiz..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=(
                        f"Create a 5-question multiple-choice quiz on '{quiz_topic}'. "
                        "Include four options (A, B, C, D) and provide the correct answers at the end."
                    )
                )

            st.success("Quiz Generated!")
            st.write(response.output_text)

# -------------------- TAB 4: Flashcards --------------------
with tab4:
    st.header("Flashcards Generator")
    flash_topic = st.text_input("Enter topic for flashcards:")

    if st.button("Generate Flashcards"):
        if flash_topic.strip() == "":
            st.warning("Please enter a topic!")
        else:
            with st.spinner("Generating flashcards..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=(
                        f"Create 5 flashcards for the topic '{flash_topic}'. "
                        "Format each as:\nTerm:\nDefinition:"
                    )
                )

            st.success("Flashcards Ready!")
            st.write(response.output_text)
