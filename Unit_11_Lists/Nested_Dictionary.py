grades = {
    'John Ponting': {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = input("Enter student's name: ")

while user_input != "exit":
    Homeworks = grades[user_input]["Homeworks"]
    Midterms = grades[user_input]["Midterm"]
    Finals = grades[user_input]["Final"]
    for hw, gd in enumerate(Homeworks):
        print(f"Homework:{hw} Grades {gd}")
        print(f"Midterms: {Midterms}")
        print(f"Finals: {Finals}")
    user_input = input("Enter a student's name or exit to quit: ")
