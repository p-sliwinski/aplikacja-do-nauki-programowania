import json

def python_quiz():
    with open("../data/python_quiz.json", "r", encoding="utf-8") as file:
        questions = json.load(file)

    score = 0
    print("")
    print("Quiz Python")

    for q in questions:
        print("")
        print(q["question"])
        answer = input("Odpowiedz: ")

        if answer == q["answer"]:
            print("Dobrze")
            score = score + 1

        if answer != q["answer"]:
            print("Zle")
            print("Poprawna:", q["answer"])

    print("")
    print("Wynik:", score, "/", len(questions))


def js_quiz():
    with open("../data/js_quiz.json", "r", encoding="utf-8") as file:
        questions = json.load(file)

    score = 0
    print("")
    print("Quiz JavaScript")

    for q in questions:
        print("")
        print(q["question"])
        answer = input("Odpowiedz: ")

        if answer == q["answer"]:
            print("Dobrze")
            score = score + 1

        if answer != q["answer"]:
            print("Zle")
            print("Poprawna:", q["answer"])

    print("")
    print("Wynik:", score, "/", len(questions))