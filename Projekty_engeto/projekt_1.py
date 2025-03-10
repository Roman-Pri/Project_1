"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ing. Roman Příhonský, MMS, MSS
email:  roman.prihonsky83@gmail.com
"""
# Initial data


TEXTS = [
    """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
]
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}
min_values = 1
max_values = len(TEXTS)
separator = "*" * 50
attempts = 3
# Main body of program - Inital enter


while attempts > 0:
    username = input("Username:")
    password = input("Password:")
    if (
        registered_users.get(username)
        and registered_users[username] == password
    ):
        print(separator)
        print(
            f"""Welcome to our company TEXT ANALYZER, {username.upper()}.
We have {max_values} text(s) available for analysis."""
        )
        print(separator)
        break
    else:
        attempts = attempts - 1
        if attempts == 0:
            print(separator)
            print(
                """Unregistered username or password.
Please contact the company administrator.
Terminating of the program..."""
            )
            print(separator)
            exit()
        print(separator)
        print(
            f"""You insert unregistered name or password.
You have {attempts} attempts left."""
        )
        print(separator)
while True:
    selection = input(
        f"Please enter an integer from {min_values} to {max_values} to select text:"
    )
    if not selection.strip().isdigit():
        print(separator)
        print("An invalid symbol was entered.Terminating of the program...")
        print(separator)
        break
    elif min_values <= int(selection) <= max_values:
        # formulas for text analysis

        selection_number = int(selection)
        words = TEXTS[selection_number - 1].split()
        number_of_words = len(words)
        number_of_tc_words = len([word for word in words if word.istitle()])
        number_of_uc_words = len(
            [
                word
                for word in words
                if word.strip(".,!?;:").isupper() and word.isalpha()
            ]
        )
        number_of_lc_words = len(
            [word for word in words if word.strip(".,!?;:").islower()]
        )
        number_of_num_strings = len([word for word in words if word.isdigit()])
        sum_of_numbers = sum([int(num) for num in words if num.isdigit()])
        print(separator)
        print(f"You have selected the text number:{selection_number}")
        print(f"There are {number_of_words} words in the selected text.")
        print(f"There are {number_of_tc_words} titlecase words.")
        print(f"There are {number_of_uc_words} uppercase words.")
        print(f"There are {number_of_lc_words} lowercase words.")
        print(f"There are {number_of_num_strings} numeric strings.")
        print(f"The sum of all numbers is {str(sum_of_numbers)}.")
        print(separator)
        # graphic representation

        occurrences = "OCCURRENCES"
        length_counts = {}
        for word in words:
            length = len(word.strip(".,!?;:"))
            length_counts[length] = length_counts.get(length, 0) + 1
        print(f"LEN|{occurrences:-^20}|NR")
        for length in sorted(length_counts):
            count = length_counts[length]
            print(f"{length:>3}|{'#' * count:<20}|{count:<3}")
        print(separator)
        # return to analysis of selected texts

        while True:
            answer = input(
                "Do you want to continue analyzing other texts (yes/no)?"
            )
            if answer.lower().strip() == "no":
                print("Terminating of the program.")
                print(separator)
                exit()
            elif answer.lower().strip() == "yes":
                break
            else:
                print("An invalid input.")
    else:
        print(separator)
        print(
            """The incorrect integer was entered.
Terminating of the program..."""
        )
        print(separator)
        exit()

# Do programu jsem si přidal několik dalších vylepšení, 
# abych si ho vylepšil pro mé budoucí portfólio a hlavně procvičil smyčku while.
# Přidal jsem:
# 1. 3 pokusy pro úvodní vstup,
# 2. Opětovné nabídnutí analýzi textů.
# Hlavním cílem bylo splnit zadání, kde se vše po špatném zadání ukončovalo. 
# Přidané while smyčky dávají opakující možnost, a uvědomuji si, 
# že program není konsistentní vzhledem k ukončování.

# Díky za feedback
# S pozdravem Roman