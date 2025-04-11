#define quiz creator program
def quiz_creator():
    #create a file path or directory for the txt file
    filename = "quiz_questions.txt"
    #overwrite content in file and assign the file object as file
    with open(filename, "w") as file:
        #loop the program until user wants to exit
        while True:
            #ask the user for quiz questions
            questions = input("Enter the quiz question (Press 'e' to exit): ")
            if questions.lower() == 'e':
                print("Exiting the program.")
                break
            #ask for the choices
            choice_a = input("Enter choice a: ")
            choice_b = input("Enter choice b: ")
            choice_c = input("Enter choice c: ")
            choice_d = input("Enter choice d: ")
            #ask for the correct answer
            #save all the data to the txt file