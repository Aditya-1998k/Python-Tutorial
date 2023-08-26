"""
Create a program capable of displaying questions to 
user like kbc
Use list data type to store the questions and their correct
answers
display the final amount the person is taking home after
playing the game
"""

questions =[
    "Who is PM OF India: 1.Narendra Modi 2.Yogi Ji ",
    "Who is Current CM of UP: 1.Nithis 2.Yogi ",
    "What is the capital city of India? 1.Delhi 2.Bengal ",
    "What is the national animal of India? 1.Lion 2.Elephant ",
    "What is the national flower of India? 1.Rose 2.Lotus ",
    "What is the name of India's national space agency? 1.Nasa 2.ISRO ",
    "Who was the first Prime Minister of India? 1.JL Nehru 2.Modi "
]

answers = [1,2,1,1,2,2,1]

def KaunBanegaCrorepati(name, questions, answers):
    prize = 0
    for i in range(len(questions)):
        que = int(input(questions[i]))
        if que == answers[i]:
            prize +=1000000
        else:
            if (prize < 3000000):
                return name," You have earned Nothing"
            else:
                return "Hurray",name, "You have earned: ",prize, "Rupees"
    msg ="Hey", name, "You are the Winner You earned :" ,prize
    return msg
            
name=input("Enter Your Name: ")
print(KaunBanegaCrorepati(name, questions, answers))