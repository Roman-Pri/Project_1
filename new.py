import random
import datetime
import tkinter as tk

def run_new_game():
    for widget in window.winfo_children():
        widget.destroy()

    # Reset časovače
    window.stop_timer = False  
    window.start_time = None  

    # Vygenerování nového tajného čísla
    secret_number = generate_secret_number()
    guesses = 0  

    # Úvodní label
    gra_for = "-" * 64
    opening_text_label = ("Hi there!\n" + 
        gra_for + 
        "\nI've generated a random 4 digit number for you.\n"
        "Let's play Bulls and Cows game.\n" +
        gra_for +
        "\nInsert the number and press Enter button:"
    )
    label = tkinter.Label(window, text=opening_text_label, font=("Arial", 20), background="green", justify="left")
    label.place(x=10, y=10)

    # Pole pro hádání
    entry = tkinter.Entry(window, font=("Arial", 16), width=10)
    entry.place(x=10, y=220)

    # Label pro čas
    time_label = tkinter.Label(window, text="Game Time - 0:00", font=("Arial", 30), background="green", justify="right")
    time_label.place(x=940, y=10)

    # Listbox pro zobrazení předešlých hádání
    guesses_listbox = tkinter.Listbox(window, font=("Arial", 14), width=50, height=10)
    guesses_listbox.place(x=10, y=300)

    # Funkce pro kontrolu hádání (bez globálního přístupu)
    def check_guess(secret_number):
        nonlocal guesses
        guess = entry.get()

        # Ověření hádání
        is_valid, error_message = validate_guess(guess)
        if not is_valid:
            label.config(text=error_message)
            return

        guesses += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        # Přidání do listboxu
        guesses_listbox.insert(tkinter.END, f"Guess {guesses}: {guess} -> {bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")

        # Výhra
        if bulls == 4:
            label.config(text=f"Correct, you've guessed the right number in {guesses} guesses!\nGame Over!")
            stop_stopwatch(time_label, window)  # Zastavení časovače
        else:
            label.config(text=f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")

    # Funkce pro start časovače při prvním pokusu
    def start_on_submit():
        start_stopwatch(time_label, window)
        check_guess(secret_number)  # Předáváme tajné číslo

    # Tlačítko pro odeslání hádání
    submit_button = tkinter.Button(window, text="Submit Guess", font=("Arial", 16), command=start_on_submit)
    submit_button.place(x=10, y=250)



