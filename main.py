from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for values in question_data:
    q_question = values["question"]
    q_answer = values["correct_answer"]
    new_question = Question(q_question, q_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print("You have completed the quiz")
    print(f"Your final score is: {quiz.current_score}/{quiz.question_number}")






