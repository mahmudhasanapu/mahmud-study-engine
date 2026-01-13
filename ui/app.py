import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.flashcard_service import FlashcardService



# Streamlit import
import streamlit as st

# Import your services (Flashcard, Quiz, Summary)
from services.flashcard_service import FlashcardService
from services.quiz_service import QuizService
from services.summary_service import SummaryService

# Page configuration
st.set_page_config(
    page_title="AI Study Engine",  # Browser tab title
    layout="wide"  # Wider layout for better UI
)

# Main title
st.title("AI Study Engine")
st.markdown("Generate Flashcards, Quizzes, and Summaries from any text!")


# Dropdown to select feature
feature = st.selectbox(
    "Choose Feature",
    ["Flashcards", "Quiz", "Summary"]
)

# Large text area for user input
text_input = st.text_area(
    "Enter your study text here",  # Placeholder
    height=200  # Height in pixels
)

# Button to generate output
if st.button("Generate"):

    # Check if user entered text
    if not text_input.strip():
        st.warning("Please enter some text!")
    else:
        # Decide which service to call based on selected feature
        if feature == "Flashcards":
            service = FlashcardService()
            output = service.generate_flashcards(text_input)

        elif feature == "Quiz":
            service = QuizService()
            output = service.generate_quiz(text_input)

        elif feature == "Summary":
            service = SummaryService()
            output = service.generate_summary(text_input)

        else:
            output = "Invalid Feature"

        # Display the output in JSON format
        st.subheader(f"{feature} Output")
        st.json(output)



