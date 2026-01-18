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

        for i in range(len(q["options"])):
            print(f"{i + 1}. {q['options'][i]}")

        answer = input("Odpowiedź (numer): ")

        if int(answer) - 1 == q["answer"]:
            print("Dobrze")
            score = score + 1
        else:
            print("Źle")
            print("Poprawna:", q["answer"] + 1)

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

        for i in range(len(q["options"])):
            print(f"{i + 1}. {q['options'][i]}")

        answer = input("Odpowiedź (numer): ")

        if int(answer) - 1 == q["answer"]:
            print("Dobrze")
            score = score + 1
        else:
            print("Źle")
            print("Poprawna:", q["answer"] + 1)

    print("")
    print("Wynik:", score, "/", len(questions))
