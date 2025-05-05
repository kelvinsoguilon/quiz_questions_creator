#select file to load and read it
def load_questions_with_answers(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines() 

    #store the questions and answers
    questions = []
    answers = {}
    #determine how the questions and answers are stored in the txt file
#parse the questions
#parse the answers
#randomly select the questions
#score counter