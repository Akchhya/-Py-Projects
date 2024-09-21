from question_model import Question
from data import question_data
question_bank=[]
for ques in question_data:
    ques_text = question_data["text"]
    ques_ans = question_data["answer"]
    new_ques = Question(ques_text , ques_ans)
    question_bank.append(new_ques)