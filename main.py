questions =[ ["What is the national bird of India?","Peacock","Sparrow",
             "Eagle","Crow","None",1],

             ["Which is the Most Subscribers in this  Youtube Channels in India?","Carryminaty","Total gaming",
             "Set TV","Round2hell","None",3],

             ["Which language is used to make games?","python","java","C++",
              "Java Script","none",3],

             ["Which Channel is break all youtube channels recoards","Mr. Beast","U R Cristiano","T-Series","Set TV"
              ,"none",2],

             ["Which is the highest earning movie in the world","Avengers Endgame","Avtaar","Titanic","Avtaar 2"
              ,"none",2],
             ["What is the national bird of India?","Peacock","Sparrow",
             "Eagle","Crow","None",1],

             ["Which is the Most Subscribers in this  Youtube Channels in India?","Carryminaty","Total gaming",
             "Set TV","Round2hell","None",3],

             ["Which language is used to make games?","python","java","C++",
              "Java Script","none",3],

             ["Which Channel is break all youtube channels recoards","Mr. Beast","U R Cristiano","T-Series","Set TV"
              ,"none",2],

             ["Which is the highest earning movie in the world","Avengers Endgame","Avtaar","Titanic","Avtaar 2"
              ,"none",2],

             ["What is the national bird of India?","Peacock","Sparrow",
             "Eagle","Crow","None",1],

             ["Which is the Most Subscribers in this  Youtube Channels in India?","Carryminaty","Total gaming",
             "Set TV","Round2hell","None",3],

             ["Which language is used to make games?","python","java","C++",
              "Java Script","none",3],

             ["Which Channel is break all youtube channels recoards","Mr. Beast","U R Cristiano","T-Series","Set TV"
              ,"none",2],

             ["Which is the highest earning movie in the world","Avengers Endgame","Avtaar","Titanic","Avtaar 2"
              ,"none",2],

             ["What is the national bird of India?","Peacock","Sparrow",
             "Eagle","Crow","None",1],

             ["Which is the Most Subscribers in this  Youtube Channels in India?","Carryminaty","Total gaming",
             "Set TV","Round2hell","None",3],

             ["Which language is used to make games?","python","java","C++",
              "Java Script","none",3],

             ["Which Channel is break all youtube channels recoards","Mr. Beast","U R Cristiano","T-Series","Set TV"
              ,"none",2],

             ["Which is the highest earning movie in the world","Avengers Endgame","Avtaar","Titanic","Avtaar 2"
              ,"none",2]
]

levels = [10000,20000,30000,50000,100000,200000,400000,800000,1600000,3200000
          ,640000,1250000,2500000,5000000,10000000,70000000]

for i in range (0, len(questions)):
    question = questions[i]
    print(f"\nquestion for Rs.{levels[i]}\n")

    print(f"{question[0]}")
    print(f"a.{question[1]}                        b.{question[2]}")
    print(f"c.{question[3]}                          d.{question[4]}")
    reply = int (input("Enter your answer (1-4)"))
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")

        if (i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i ==14):
            money = 10000000
        elif(i == 15):
            money = 70000000
    else:
        print("Wrong answer!")
        break