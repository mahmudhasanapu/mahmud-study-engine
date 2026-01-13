# from services.flashcard_service import FlashcardService

# text = """
# Machine learning is a field of artificial intelligence.
# It allows systems to learn from data.
# Supervised learning uses labeled data.
# Unsupervised learning uses unlabeled data.
# """

# service = FlashcardService()
# result = service.generate_flashcards(text)

# print(result)


# from services.quiz_service import QuizService

# if __name__ == "__main__":
#     text = """
#     Machine learning is a branch of artificial intelligence.
#     It allows machines to learn from data.
#     Supervised learning uses labeled data.
#     Unsupervised learning works with unlabeled data.
#     Overfitting happens when a model memorizes training data.
#     """

#     quiz_service = QuizService()
#     result = quiz_service.generate_quiz(text)

#     print("====== QUIZ OUTPUT ======")
#     print(result)

# from services.summary_service import SummaryService

# notes_text = """
# Machine learning is a field of artificial intelligence.
# It allows systems to learn from data.
# Supervised learning uses labeled data.
# Unsupervised learning works with unlabeled data.
# Overfitting happens when a model memorizes the training data.
# """

# summary_service = SummaryService()
# summary_output = summary_service.generate_summary(notes_text)

# print("====== SUMMARY OUTPUT ======")
# print(summary_output)



from services.evaluation_service import EvaluationService

if __name__ == "__main__":
    service = EvaluationService()

    result = service.evaluate(
        question="What is machine learning?",
        correct_answer="A branch of artificial intelligence that learns from data",
        user_answer="Machine learning teaches computers using data"
    )

    print("=== EVALUATION RESULT ===")
    print(result)



