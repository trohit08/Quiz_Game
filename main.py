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
    4. There will be question followed by four options, you have to choose right answers.''')

#----------------------------------------------------------------------------------------

def play():
    
    questions = []
    op1 = []
    op2 = []
    op3 = []
    op4 = []
    answers = []
    #count length of lines in document
    count = len(open('capital_ques.txt').readline())
    with open('capital_ques.txt','r') as file:  #read file
        for f in islice(file,1,count):  #sliceed the line from 2nd line to last line
            wor = [s.strip() for s in f.split(',')] #remove spaces and split the line from somepoint
            
            questions.append(wor[0])
            op1.append(wor[1])
            op2.append(wor[2])
            op3.append(wor[3])
            op4.append(wor[4])
            answers.append(wor[5])

    no_of_quiz = int(input('How many question should be there in your quiz = '))

    count = 0
    for i in range(no_of_quiz):
        j = random.randint(1,no_of_quiz)
        print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(questions[j])
        print(op1[j])     
        print(op2[j])
        print(op3[j])
        print(op4[j])

        ans = input('YOUR ANSWER FROM ABOVE OPTIONS (write it down your whole answer) : ')
        
        if ans.lower() == answers[j].lower():
            count += 5
            print('\ncorrect')
        else :
            if no_of_quiz != 1:
                count -= 2
                print('\nIncorrect')
                print('\nCorrect answer is :', answers[j].capitalize())
    
    print('Your Score Is : ',count)


#------------------------------------------------------------------------------------------------------------

print('\n ===============Welcome To The Game================')
print('\n1. Start Game')
print('2. Rules')
print('3. About')

choice = int(input('\n\n ~~~~Enter Your choice :') )

if choice == 1:
    play()
if choice == 2:
    rules()
if choice == 3:
    about()


