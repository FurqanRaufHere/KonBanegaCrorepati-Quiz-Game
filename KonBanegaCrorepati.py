# Kon banega crorepati mini project
questions = [
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "PHP", 4],  # PHP is correct
    ["Which language was used to create insta?", "Python", "French", "JavaScript", "PHP", 1],  # Python is correct
    ["Which language was used to create LinkedIn?", "Python", "French", "JavaScript", "PHP", 3],  # JavaScript is correct
    ["Which language was used to create Twitter?", "Python", "French", "JavaScript", "Ruby", 4],  # Ruby is correct
    ["Which language was used to create YouTube?", "Python", "French", "JavaScript", "C++", 4],  # C++ is correct
    ["Which language was used to create WhatsApp?", "Erlang", "French", "JavaScript", "PHP", 1],  # Erlang is correct
    ["Which language was used to create SnapChat?", "Python", "French", "JavaScript", "PHP", 1],  # Python is correct
    ["Which language was used to create Tumblr?", "Python", "French", "JavaScript", "PHP", 3],  # JavaScript is correct
    ["Which language was used to create Reddit?", "Python", "French", "JavaScript", "Lisp", 1],  # Python is correct
    ["Which language was used to create Pinterest?", "Python", "French", "JavaScript", "Java", 4],  # Java is correct
    ["Which language was used to create Quora?", "Python", "French", "JavaScript", "PHP", 1],  # Python is correct
    ["Which language was used to create TikTok?", "Python", "French", "JavaScript", "PHP", 3],  # JavaScript is correct
    ["Which language was used to create Spotify?", "Python", "French", "Java", "PHP", 1],  # Python is correct

]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 1000000, 1250000, 2500000, 5000000, 100000000 ]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]} ")
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")

    reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    if(reply == 0):
        money = levels[i-1]
        break
    if reply == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i==4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong Answer!")
        break

print(f"The money you are taking home is {money} ")