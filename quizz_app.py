print("---Quiz App By Sohail---")
# store some questions its option and its correct answers.
quizes = [
    {
        "question": "What is the capital of Pakistan?",
        "options": {
            "A": "Lahore",
            "B": "Karachi",
            "C": "Islamabad",
            "D": "Peshawar"
        },
        "answer": "C"
    },
    {
        "question": "What is the capital of Russia?",
        "options": {
            "A": "Islamabad",
            "B": "Egypt",
            "C": "Moscow",
            "D": "Washington"
        },
        "answer": "C"
    },
        {   "question": "What is the Capital of Bangladesh?",
        "options": {
            "A": "Karachi",
            "B": "Dhaka",
            "C": "Wasayeepur",
            "D": "Haryana"
        },
        "answer": "B"
    }
]

# this function run the quize question/option in order
# Things is used in  it is nested loop
# Conditions
#Score tracking
def run_quize():
    score = 0
    for i in range (len(quizes)):
        print (quizes[i]["question"])#for printing questions
        for key, value in quizes[i]["options"].items():# for printing option
            print(f"{key} : {value}")# for printing question and option both
        user_input = input("Enter your Option : ").upper()
        if user_input not in ["A","B","C","D"]:
            print("Invalid option! Please enter A, B, C or D")        
        elif user_input == quizes[i]["answer"]:
            print("Correct Answer")
            score += 1
            
        else:
            print("Wrong Answer!!!")
    print(f"\n Quizz Done! Your total Score is {score}/{len(quizes)}")

# this function store question from user its option and correct answer
def question_add():
    questions = input("Enter your Question : ").capitalize()#capitalize is used for converting first letter capital
    if questions == "":
        print("Question cannot be empty!")
        return  # stops the function
    option1 = input("Please enter your first option : ").capitalize()
    option2 = input ("Please enter your Second option : ").capitalize()
    option3 = input("Please enter your Third option : ").capitalize()
    option4 = input("Please enter your fourth option : ").capitalize()
    correct_option = input("Which answer is Correct? A/B/C/D: ").upper()
    if correct_option not in ["A","B","C","D"]:
        print("Correct answer must be A, B, C or D!")
        return
    add = {            # making a nested dictionary for storing quizes
    "question": questions,
    "options": {
        "A": option1,
        "B": option2,
        "C": option3,
        "D": option4
    },
    "answer": correct_option
} 
    quizes.append(add) # append is used to add dictionary to the main quizes section
    print("Your Question added Successfully! ")

# this function show menu and excute eaxcute each option 
#condition is used to call functions
# using a while a loop for keep the program continue
def show_menu():
    while True:
        print("1. Start the Challenge")
        print("2.Rules and Regulation")
        print("3.Add Manually Questions")
        print("4.Exit")
        user = input("Enter Your Number Which you want: ")
        if user == "1":
            print("Your Challenge is start")
            run_quize()
        elif user == "2":
            
            print("Rules and Regulations")
            
            print("Number # 1: 1 score is deducted in 1 wrong answer \nNumber # 2: No Cheating\nNumber # 3: 3 option is wrong and 1 is correct ")
        elif user == "3":
            question_add()
        elif user == "4":
            print("You Exit Succussfully..!")
            break # break is used to exit while loop 
        else:
            print("Wrong Option..")
show_menu()