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
            while True:
                correct_answer = input("Enter the correct answer (a, b, c, or d): ").lower()
                if correct_answer in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print("Invalid input. Enter a, b, c, or d only.")
            #save all the data to the txt file
            file.write(questions "\n")
            file.write("a." + choice_a + "\n")
            file.write("b." + choice_b + "\n")
            file.write("c." + choice_c + "\n")
            file.write("d." + choice_d + "\n")
            file.write("Answer:" + correct_answer + "\n")
            file.write("\n")

if __name__ == "__main__":
    quiz_creator()