import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from services.flashcard_service import FlashcardService
from services.quiz_service import QuizService
from services.summary_service import SummaryService
from services.evaluation_service import EvaluationService


st.set_page_config(
    page_title="Mahmud’s Study Engine",
    layout="wide"
)

st.title("Mahmud’s Study Engine")
st.markdown("Generate Flashcards, Quizzes, and Summaries from any text!")

feature = st.selectbox(
    "Choose Feature",
    ["Flashcards", "Quiz", "Summary", "Answer Evaluation"]
)

if feature != "Answer Evaluation":

    text_input = st.text_area(
        "Enter your study text here",
        height=200,
        key="study_text"
    )

    if st.button("Generate"):

        if not text_input.strip():
            st.warning("Please enter some text!")
        else:
            if feature == "Flashcards":
                service = FlashcardService()
                output = service.generate_flashcards(text_input)

            elif feature == "Quiz":
                service = QuizService()
                output = service.generate_quiz(text_input)

            elif feature == "Summary":
                service = SummaryService()
                output = service.generate_summary(text_input)

            st.subheader(f"{feature} Output")
            st.json(output)


else:
    st.subheader("Answer Evaluation")

    question = st.text_input("Enter the question", key="eval_q")
    correct_answer = st.text_area("Enter the correct answer", key="eval_correct")
    user_answer = st.text_area("Enter the user's answer", key="eval_user")

    if st.button("Evaluate Answer"):
        if not question or not correct_answer or not user_answer:
            st.warning("Please fill in all fields!")
        else:
            service = EvaluationService()
            result = service.evaluate(
                question=question,
                correct_answer=correct_answer,
                user_answer=user_answer
            )

            st.subheader("Evaluation Result")
            st.json(result)


