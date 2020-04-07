from itertools import islice
import random

#-----------------------------------------------------------------------------------------------

def about():
    print('''\n    ============About============
        
        Hi my name is Rohit and this game is made by me. ''')

#--------------------------------------------------------------------------------------------------

def rules():
    print('''\n ==============Rules==============
    Quiz game rules  are:-
    1. For each correct answer you will get 5 points.
    2. For each wrong answer you will deduct minus 2.
    3. You must write the whole answer which is already in options.
    4. There will be question followed by four options, you have to choose right answers.
    5. If your most of the answers are wrong then you will get negative points.''')

#----------------------------------------------------------------------------------------

def play():
    #defined empty lists
    questions = []
    op1 = []
    op2 = []
    op3 = []
    op4 = []
    answers = []
    #count length of lines in document
    count = len(open('capital_ques.txt').readline())
    with open('capital_ques.txt','r') as file:  #read the file
        for f in islice(file,1,count):  #sliced the line from 2nd line to last line
            wor = [s.strip() for s in f.split(',')] #remove spaces and split the line from somepoint
            
            #appended questions, options and answers into empty lists 
            questions.append(wor[0])
            op1.append(wor[1])
            op2.append(wor[2])
            op3.append(wor[3])
            op4.append(wor[4])
            answers.append(wor[5])
    #input from user
    no_of_quiz = int(input('How many question should be there in your quiz = '))

    #print questions with options
    count = 0
    for _ in range(no_of_quiz):
        j = random.randint(1,no_of_quiz)
        print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(questions[j])
        print(op1[j])     
        print(op2[j])
        print(op3[j])
        print(op4[j])

        ans = input('YOUR ANSWER FROM ABOVE OPTIONS (write it down your whole answer) : ')  #user answer
        
        if ans.lower() == answers[j].lower():  #comparing answers in lower case
            count += 5   #counting points for right answers
            print('\ncorrect')
        else :
            count -= 2  #negative markings for wrong answers
            print('\nIncorrect')
            print('\nCorrect answer is :', answers[j].capitalize())
    
    print('\nYour Score Is : ',count)


#------------------------------------------------------------------------------------------------------------

#initialization point
print('\n ===============Welcome To The Game================')
print('\n1. Start Game')
print('2. Rules')
print('3. About')

choice = int(input('\n\n ~~~~Enter Your choice :') )  #input from user

if choice == 1:
    play()
if choice == 2:
    rules()
if choice == 3:
    about()


