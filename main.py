questions =[ ["Which is the largest lake in the world","Capsian sea","Biakal","Malawi","Grate slave lake"
              ,"none",1],

             ["Which planet in the solar system is known as \"Red planet\" ","Venus","Earth","Mars","Jupoter"
              ,"none",3],

             ["Which language is used to make games?","python","java","C++",
              "Java Script","none",3],

             ["Which is the largest ocean in the world?", "Indian ", "pecific",
              "Atlantic", "Arctic", "None", 2],

             ["Which is the highest grossing movie in the world","Avengers Endgame","Avtaar","Titanic","Avtaar 2"
              ,"none",2],

             ["In Olympic flag red color represent?","Asia","America",
             "Ausrralia","Europe","None",2],

             ["Who designed the Naational Flag of  India?","Bankim Chandra Chattopadhyay","Jadunath Bhattacharya",
             "Ravindranath Tagore","Pingali Vankayya","None",4],

             ["How many words in Original National Anthem?","214","215","216",
              "217","none",3],

             ["Who is the father of python","Guido Van Rossum","Tim Berners-Lee","James Goslin","Bjarne Stroustrup"
              ,"none",1],

             ["Who is the father of C","Tim Berners-Lee","Dennis Ritchie","James Goslin","Brendan Eich"
              ,"none",2],

             ["How many elements are in the priodic table?","118","119",
             "120","121","None",1],

             ["How many hearts does an octopos have ?","1","2",
             "3","4","None",3],

             ["In which year was the first olympic games held ?","1896","1892","1898",
              "1994","none",1],

             ["When was first man sent to space","1960","1961","1962","1963"
              ,"none",2],

             ["Where was the invent of exam","Japan","China","Russia","Britain"
              ,"none",2],

             ["Who invent Exam?","Henry Fischel","Me",
             "Roberto Nevelis","Hen nevon","None",1],
]

levels = [10000,20000,30000,50000,100000,200000,400000,800000,1600000,3200000
          ,640000,1250000,2500000,5000000,10000000,70000000]
count=0
for j in range (0, len(questions)):
    question = questions[j]
    count+=1
    print(f"\nquestion for Rs.{levels[j]}\n")

    print(f"{count}. {question[0]}")
    print(f"1.{question[1]}                        2.{question[2]}")
    print(f"3.{question[3]}                          4.{question[4]}")
    reply = int (input("  answer =  "))
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs.{levels[j]}\n\n")

        if (j==4):
            money = 10000
        elif(j == 9):
            money = 320000
        elif(j == 14):
            money = 10000000
        elif(j == 15):
            money = 70000000
    else:
        print("Wrong answer!")
        break
