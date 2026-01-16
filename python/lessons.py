import json

def show_python_lessons():
    with open("../data/python_lessons.json", "r", encoding="utf-8") as file:
        lessons = json.load(file)

    print("")
    print("Lekcje Python")

    for lesson in lessons:
        print("")
        print("Lekcja", lesson["id"], "-", lesson["title"])
        print(lesson["content"])
        input("Enter aby dalej...")

def show_js_lessons():
    with open("../data/js_lessons.json", "r", encoding="utf-8") as file:
        lessons = json.load(file)

    print("")
    print("Lekcje JavaScript")

    for lesson in lessons:
        print("")
        print("Lekcja", lesson["id"], "-", lesson["title"])
        print(lesson["content"])
        input("Enter aby dalej...")