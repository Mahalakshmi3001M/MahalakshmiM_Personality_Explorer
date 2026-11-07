import streamlit as st
import requests

st.set_page_config(
    page_title="Personality Explorer",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Personality Explorer")
st.write("Answer the questions below to discover your personality type!")

descriptions = {
    "explorer": "🌍 **Explorer** – You are curious, adventurous and love new experiences.",
    "thinker":  "🧠 **Thinker** – You are logical, analytical and enjoy deep knowledge.",
    "leader":   "👑 **Leader** – You are confident, social and good at guiding people.",
    "creator":  "🎨 **Creator** – You are imaginative, original and love expressing ideas."
}

with st.form("personality_form"):
    name = st.text_input("Your Name", placeholder="Enter your name")
    age = st.number_input("Your Age", min_value=10, max_value=100, value=20)

    st.subheader("1. How do you spend your free time?")
    q1 = st.radio(
        "Choose one:",
        options=[
            "Travelling or trying new things",
            "Reading or learning something",
            "Hanging out and organising friends",
            "Drawing, writing or making things"
        ],
        key="q1"
    )

    st.subheader("2. How do you solve problems?")
    q2 = st.radio(
        "Choose one:",
        options=[
            "Try different things until one works",
            "Analyse step by step",
            "Take charge and assign tasks",
            "Come up with an original idea"
        ],
        key="q2"
    )

    st.subheader("3. Pick your ideal weekend")
    q3 = st.selectbox(
        "Choose one:",
        options=[
            "Trekking in a new place",
            "Solving puzzles at home",
            "Planning a group event",
            "Working on a personal project"
        ]
    )

    st.subheader("4. Which words describe you? (Select all that apply)")
    q4 = st.multiselect(
        "Select all that apply:",
        options=["Adventurous", "Logical", "Confident", "Imaginative"]
    )

    submitted = st.form_submit_button("Find My Personality", use_container_width=True)

if submitted:
    if not name.strip():
        st.warning("Please enter your name.")
    else:
        score = {"explorer": 0, "thinker": 0, "leader": 0, "creator": 0}

        mapping = {
            "Travelling or trying new things": "explorer",
            "Reading or learning something": "thinker",
            "Hanging out and organising friends": "leader",
            "Drawing, writing or making things": "creator",
            "Try different things until one works": "explorer",
            "Analyse step by step": "thinker",
            "Take charge and assign tasks": "leader",
            "Come up with an original idea": "creator",
            "Trekking in a new place": "explorer",
            "Solving puzzles at home": "thinker",
            "Planning a group event": "leader",
            "Working on a personal project": "creator",
            "Adventurous": "explorer",
            "Logical": "thinker",
            "Confident": "leader",
            "Imaginative": "creator"
        }

        score[mapping[q1]] += 1
        score[mapping[q2]] += 1
        score[mapping[q3]] += 1
        for item in q4:
            score[mapping[item]] += 1

        top = max(score, key=score.get)

        st.success(f"Hello, **{name}**!")
        st.markdown(descriptions[top])

        # Fetch random quote
        try:
            res = requests.get("https://dummyjson.com/quotes/random", timeout=5)
            if res.status_code == 200:
                data = res.json()
                st.info(f"💬 **Quote for you:**\n\n*“{data['quote']}”*\n\n— **{data['author']}**")
            else:
                st.warning("Could not load a quote right now.")
        except:
            st.warning("Could not load a quote right now.")