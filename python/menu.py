from lessons import show_python_lessons, show_js_lessons
from quiz import python_quiz, js_quiz

def show_menu():
    print("")
    print("1. Nauka Python")
    print("2. Quiz Python")
    print("3. Nauka JavaScript")
    print("4. Quiz JavaScript")
    print("0. Wyjscie")

    choice = input("Wybierz opcje: ")

    if choice == "1":
        show_python_lessons()

    if choice == "2":
        python_quiz()

    if choice == "3":
        show_js_lessons()

    if choice == "4":
        js_quiz()

    if choice == "0":
        print("Do widzenia")