import os
import csv
from os import walk


def start():
    menu_input = input("""Welcome to flashcard app!
What do you want to do?
    (1) Create new deck
    (2) Choose existing deck
    Press any other button to quit
""")

    menu_input = str_to_int(menu_input)

    if menu_input == 1: return new_deck()
    elif menu_input == 2: return choose_deck()
    return

def new_deck():
    checking_for_dir()
    deck_name = input("Set the name of your deck:  ")
    while deck_name == '':
        deck_name = input("Please enter a correct name:  ")
    return creating_deck(deck_name)

def creating_deck(deck_name):
    print(f"""You are creating a new deck called {deck_name}!""")
    print("Leave blank space in the question input to stop adding new flashcards")

    deck_header = ['question','answer']
    deck_rows = []
    question = None
    answer = None

    file = open(f'./flashcards/{deck_name}.csv', 'w',newline='')
    writer = csv.writer(file)
    writer.writerow(deck_header)

    while question != '' and answer != '':
        question = input("Question: ")
        if question == '': break
        answer = input("Answer: ")
        deck_row = [question, answer]
        deck_rows.append(deck_row)
        deck_row = []
    writer.writerows(deck_rows)
    file.close()

    menu_input = input("""    (1) Save and go back
    Press any other button to quit
""")

    menu_input = str_to_int(menu_input)

    if menu_input == 1: return start()
    return

def choose_deck():
    checking_for_dir()
    if os.listdir("./flashcards/"):
        filenames = next(walk("./flashcards/"), (None, None, []))[2]
        
        for number in range(0,len(filenames)):
            print(f"    ({number+1}) {filenames[number]}")

        menu_input = input()
        menu_input = str_to_int(menu_input)

        for number in range(0,len(filenames)):
            if menu_input == number+1: study(filenames[number])
        return 
    else:
        menu_input = input("""You dont have any existing decks!
    (1) Go back
    Press any other button to quit
""")

        menu_input = str_to_int(menu_input)

        if menu_input == 1: return start()
        return

def study(deck_name):
    print(f"studying: {deck_name}")
    file = open(f"./flashcards/{deck_name}", "r")
    reader = csv.reader(file)
    header = []
    header = next(reader)
    rows = []

    for row in reader:
        rows.append(row)

    for row in range(0,len(rows)):
        menu_input = input(f"""\n{header[0]}: {rows[row][0]}\n
(1) Uncover answer
(2) Go back
Press anything else to quit
""")

        menu_input = str_to_int(menu_input)

        if menu_input == 1: menu_input = input(f"""\n{header[1]}: {rows[row][1]}\n
(1) Next question
(2) Go back
Press anything else to quit
""")

        menu_input = str_to_int(menu_input)

        if menu_input == 2: 
            file.close()
            return choose_deck()

        if menu_input != 1:
            break
    file.close()
    return

def str_to_int(input):
    try: input = int(input)
    except: None 
    return input

def checking_for_dir():
    isExist = os.path.exists("./flashcards/")
    if not isExist:
        os.makedirs("./flashcards/")
    return

start()


