import json


    questions=["What's your name? ", "What is your date of birth? (MM/DD/YYYY) ", "How old are you ?","(Country,City,State98-[py4) Where do you call home ? ",
    ,"How many hours per week do you spend on your phone ?"," What app , website or program do you use the most?","What is your favorite movie?"," What's your favorite color?"]

    f = open("responses.json", "w")

    response = input(questions[0])
    print("Your name is ", response)


    response = input(questions[1])
    print(" My birthday is", response)


    response = input(questions[2])
    print(" I am " , response)


    response=input(questions[3])
    print("I am from" , response)


    response=input(questions[4])
    print(response, "hours")

    response=input(questions[5])
    print(response)


    response=input(questions[6])
    print("My favorite movie is ", response)

    response=input(questions[7])
    print(response)


        areWeFinished=input ("Do you want to quit? y/n")
        if areWeFinished =="y":
            break
    print(everyones_answers)
