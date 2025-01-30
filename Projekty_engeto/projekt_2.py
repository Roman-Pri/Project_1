"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Ing. Roman Příhonský, MMS, MSS
email:  roman.prihonsky83@gmail.com
"""

import random           # Support for random number generation
import datetime         # Support for timing operation
import tkinter as tk    # GUI

# 1. Functions for game logic


def generate_secret_number():
    while True:
        secret_number = random.sample(range(10), 4)
        if secret_number[0] != 0:
            return secret_number


def verify_guess(guess):
    if len(guess) != 4:
        return False, "Your guess must be exactly 4 digits."
    if not guess.isdigit():
        return False, "Your guess must contain only digits."
    guess_digits = [int(digit) for digit in guess]
    if len(set(guess_digits)) != len(guess_digits):
        return False, "Your guess must not contain duplicate digits."
    if guess_digits[0] == 0:
        return False, "Your guess must not start with 0."
    return True, ""


def evaluate_guess(secret_number, guess_digits):
    bulls = sum(1 for i in range(4) if secret_number[i] == guess_digits[i])
    cows = sum(
        1
        for i in range(4)
        if guess_digits[i] in secret_number
        and secret_number[i] != guess_digits[i]
    )
    return bulls, cows


# 2. Functions for stopwatch


def start_stopwatch(time_label, stopwatch):
    if stopwatch["start_time"] is None:
        stopwatch["start_time"] = datetime.datetime.now()
        stopwatch["stop_time"] = False
        update_time(time_label, stopwatch)


def stop_stopwatch(time_label, stopwatch):
    stopwatch["stop_timer"] = True
    elapsed_time = datetime.datetime.now() - stopwatch["start_time"]
    minutes, seconds = divmod(elapsed_time.seconds, 60)
    game_time = f"{minutes}:{seconds:02d}"
    time_label.config(text=f"Game Time - {game_time}")
    stopwatch["stop_timer"] = True
    return game_time


def update_time(time_label, stopwatch):
    if stopwatch["stop_timer"]:
        return
    elapsed = datetime.datetime.now() - stopwatch["start_time"]
    minutes, seconds = divmod(elapsed.seconds, 60)
    game_time = f"{minutes}:{seconds:02d}"
    time_label.config(text=f"Game Time - {game_time}")
    time_label.after(1000, update_time, time_label, stopwatch)


# 3. Game


def run_new_game(window):
    for widget in window.winfo_children():
        widget.destroy()
        
    # Stopwatch setup

    stopwatch = {"start_time": None, "stop_timer": False}
    game_state = {"guesses": 0}

    # Opening Text label

    gra_for = "-" * 64
    opening_text = (
        "Hi there!\n"
        + gra_for
        + "\nI've generated a random 4 digit number for you.\n"
        "Let's play Bulls and Cows game.\n" + gra_for + "\nGood Luck!"
    )

    text_label = tk.Label(
        window,
        text=opening_text,
        font=("Arial", 20),
        background="green",
        justify="left",
    )
    text_label.place(x=10, y=10)

    # Time label

    time_label = tk.Label(
        window,
        text="Game Time - 0:00",
        font=("Arial", 20),
        background="green",
        justify="right",
    )
    time_label.place(x=820, y=10)

    # Entry label for guessing and text for guessing label

    entry = tk.Entry(window, font=("Arial", 16), width=10)
    entry.place(x=1025, y=580)
    tk.Label(
        window,
        text="Insert the number and press Enter:",
        font=("Arial", 16),
        background="green",
    ).place(x=635, y=580)

    # Register to display all previous guesses and results + scrollbar

    guesses_register = tk.Listbox(
        window, font=("Arial", 16), width=50, height=20
    )
    guesses_register.place(x=640, y=62)
    scrollbar = tk.Scrollbar(
        window, orient="vertical", command=guesses_register.yview
    )
    guesses_register.config(yscrollcommand=scrollbar.set)
    scrollbar.place(x=1225, y=62, height=504)

    # Variables for game

    secret_number = generate_secret_number()

    def check_guess(event=None):
        guess = entry.get()

        # Guess validation

        is_valid, error_message = verify_guess(guess)
        if not is_valid:
            guesses_register.insert(tk.END, f"Invalid guess: {error_message}")
            guesses_register.yview_scroll(1, "units")
            return
        # first Enter - start stopwatch

        if stopwatch["start_time"] is None:
            start_stopwatch(time_label, stopwatch)
        game_state["guesses"] += 1
        guess_digits = [int(digit) for digit in guess]
        bulls, cows = evaluate_guess(secret_number, guess_digits)

        # register with results

        guesses_register.insert(
            tk.END,
            f"Guess {game_state['guesses']}: {guess} >>> {bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}",
        )
        guesses_register.yview_scroll(1, "units")

        if bulls == 4:
            game_time = stop_stopwatch(time_label, stopwatch)
            guesses_register.insert(
                tk.END,
                f"Correct, you've guessed the right number in {game_state['guesses']} guesses!\n",
            )
            guesses_register.yview_scroll(1, "units")
            guesses_register.insert(
                tk.END, f"Your game time is {game_time}.\n"
            )
            guesses_register.yview_scroll(1, "units")
            guesses_register.insert(tk.END, "That's amazing!")
            guesses_register.yview_scroll(1, "units")
            guesses_register.insert(tk.END, "Game over!")
            guesses_register.yview_scroll(1, "units")

            # Display New Game and End Game buttons after game ends

            tk.Button(
                window,
                text="New Game",
                font=("Arial", 20),
                width=15,
                height=2,
                command=lambda: run_new_game(window),
            ).place(x=200, y=300)
            tk.Button(
                window,
                text="End Game",
                font=("Arial", 20),
                width=15,
                height=2,
                command=window.quit,
            ).place(x=200, y=400)
            
        # Clear the entry after processing the guess

        entry.delete(0, tk.END)

    # Enter button - run game

    entry.bind("<Return>", check_guess)


# 4. GUI - inital window setup
def main():
    window = tk.Tk()
    screen_width, screen_height = (
        window.winfo_screenwidth(),
        window.winfo_screenheight(),
)
    window.title("Prepared by Roman Příhonský")
    window.geometry(f"{screen_width}x{screen_height}")
    window.configure(background="green")
    tk.Label(
        window,
        text="Welcome to BULLs & COWs game",
        font=("Arial", 40),
        background="green",
).pack(pady=10)
    tk.Button(
        window,
        text="NEW GAME",
        font=("Arial", 20),
        width=15,
        height=2,
        command=lambda: run_new_game(window),
).place(x=525, y=200)

    window.mainloop()

if __name__ == "__main__":
    main()
