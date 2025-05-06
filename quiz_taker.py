import random

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
    while i < len(lines):
        line = lines[i].strip()
        if line and line[0].isdigit() and '.' in line:
            parts = line.split('.')
            number = int(parts[0])
            ans = parts[1].strip().upper()
            answers[number] = ans
        i += 1

    return questions, answers
    
    #randomly select the questions
def run_quiz(questions, answers, num_questions=5):
    selected_questions = random.sample(questions,min(num_questions,len(questions)))
    score = 0

    for idx, q in enumerate(selected_questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        for opt in q['options']:
            print(opt)
        
        #score counter
        while True:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if user_answer in ['A','B','C','D']:
                break
            else:
                print("Invalid input. Select A/B/C/D only.")