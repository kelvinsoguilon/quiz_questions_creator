#select file to load and read it
def load_questions_with_answers(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines() 

    #store the questions and answers
    questions = []
    answers = {}
    
    #determine how the questions and answers are stored in the txt file
    i = 0
    questions_index = 1
    #parse the questions and options
    while i < len(lines):
        line = lines[i].strip()
        if line.lower().startswith("answer key:"):
            break
        if line:
            q_text = line.split('.', 1)[1].strip() if '.' in line else line
            opts = [lines[i + j].strip() for j in range(1, 5)]
            questions.append({'index': questions_index, 'question': q_text, 'options': opts})
            questions_index += 1
            i += 5 #lines in a block of question
        else:
            i += 1 #if there is empty space
    #parse the answers
#randomly select the questions
#score counter