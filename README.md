                                     Mahmud’s StudyMate AI
                                     

Mahmud’s StudyMate AI is a standalone AI-powered study content engine.  
It is designed to generate useful study materials such as flashcards, quizzes, and summaries from raw study text.

This project focuses only on the AI intelligence layer so that it can be easily integrated into any future backend or platform.


                                            Features

•	Flashcard Generation  
Generates clear question–answer pairs from any study text to help with quick revision.

•	Quiz Generation 
Create multiple-choice questions with several options and one correct answer based on   the given content.

•	Notes Summarization  
 Produces short and easy-to-understand summaries while keeping the important concepts.

•	Answer Evaluation (Optional)  
Compares a user’s answer with the correct answer and provides a score with brief feedback.

                                   Project Structure

The project is organized in a modular way to keep the AI logic clean and easy to extend.



```text
ai-study-engine/
│
├── services/
│   ├── flashcard_service.py
│   ├── quiz_service.py
│   ├── summary_service.py
│   └── evaluation_service.py
│
├── providers/
│   └── groq_provider.py
│
├── prompts/
│   ├── flashcard_prompt.py
│   ├── quiz_prompt.py
│   └── summary_prompt.py
│
├── ui/
│   └── app.py
│
├── config/
│   └── settings.py
│
├── requirements.txt
└── README.md


                                  Setup and Run Instructions

Follow the steps below to run the project locally.

1. Clone the Repository
```bash
git clone https://github.com/<your-username>/mahmud-studymate-ai.git
cd mahmud-studymate-ai

2. Create and Activate Virtual Environment
```bash
python -m venv venv

For Windows:
```bash
venv\Scripts\activate

For macOS/Linux:
```bash
source venv/bin/activate

3. Install Dependencies
```bash
pip install -r requirements.txt

4. Environment Configuration
Create a .env file in the project root and add your API key:
GROQ_API_KEY=your_api_key_here

5. Run the Application
```bash
streamlit run ui/app.py

The application will be available at:
http://localhost:8501

                             Usage Examples (Inputs & Outputs)

1. Flashcard Generation
Input: A branch of artificial intelligence that enables machines to learn from data.
       It includes supervised and unsupervised learning techniques.

Expected Output: - What is machine learning?
                 - What type of data is used in supervised learning?   

2. Quiz Generation
Input: Machine learning models are trained using data.
       Supervised learning uses labeled datasets.

Expected Output: Multiple-choice questions where each question contains:
                 - A question statement
                 - Four options
                 - One correct answer

3. Notes Summarization
Input: Machine learning is a field of artificial intelligence that focuses on building systems
       that learn from data and improve performance over time.

Expected Output: A concise summary highlighting the key concepts while removing                unnecessary details.

4. Answer Evaluation (Optional Feature)
Input: Question: What is machine learning?
       Correct Answer: A field of AI that learns from data.
       User Answer: Teaching computers using data.

Expected Output: A structured evaluation result including:
                 - Whether the answer is correct
                 - A score
                 - Short feedback


                               Architecture & Design Explanation

The project is designed with a clear separation of responsibilities to ensure
maintainability, flexibility, and ease of integration with any future backend system.

The AI-related logic is isolated from the user interface and configuration layers.
Each core feature is implemented as an independent service, allowing the system to
be extended or modified without affecting other components.


                                Folder Structure Explanation

- providers/  
  Contains the model provider logic responsible for communicating with external AI services.

- services/  
  Implements the core study features such as flashcard generation, quiz generation,
  summary creation, and answer evaluation.

- prompts/  
  Stores prompt templates separately to keep content generation rules independent
  from the application logic.

- config/  
  Handles environment-based configuration such as API keys.

- ui/  
  Contains the Streamlit-based user interface layer.


                                  Provider Flexibility

The system is structured to support multiple AI model providers.
All provider-specific logic is isolated in a dedicated layer, making it possible
to switch or extend providers without modifying the core application logic.

                                  Environment Variable

All sensitive configuration values, such as API keys, are managed through environment
variables to ensure security and environment-independent deployment.

                                     Final Notes

This project focuses only on the AI intelligence layer of a study management system.
No authentication, database, or backend framework has been included, as the goal is
to keep the system lightweight and easily integrable with any future platform.

The implementation prioritizes clean code structure, modular design, and consistent
output formats to support future extension and production usage.

                                      Live Demo

The application has been deployed using Streamlit and can be accessed via the link below:
[text](https://ai-study-engine-asrriyxappaadvcap6ymtef.streamlit.app/~/+/#mahmuds-study-engine)


                                 Submission Checklist

AI intelligence layer implemented
Modular and provider-independent design
Environment-based configuration
Clear documentation and usage examples
Live deployment link included






   





                 
















