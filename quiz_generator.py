#define quiz creator program
def quiz_creator():
    #create a file path or directory for the txt file
    filename = "quiz_questions.txt"
    #overwrite content in file and assign the file object as file
    with open(filename, "w") as file:
#loop the program until user wants to exit
#ask the user for quiz questions
#ask for the choices
#ask for the correct answer
#save all the data to the txt file