"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Ing. Roman Příhonský, MMS, MSS
email:  roman.prihonsky83@gmail.com
"""
import random           # Support for random number generation
import datetime         # Support for timing operation
import tkinter          # GUI

# Functions for gussing, validating and evaluating secret number
def generate_secret_number():
    while True:
        list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        random.shuffle(list_of_numbers)
        secret_number = list_of_numbers[:4]
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

def evaluate_guess(secret_number, guess):
    bulls = sum([1 for i in range(4) if secret_number[i] == guess[i]])
    cows = sum([1 for i in range(4) if guess[i] in secret_number and secret_number[i] != guess[i]])
    return bulls, cows

# Functions for stopwatch
def start_stopwatch(time_label, window):
    if window.start_time is None:
        window.start_time = datetime.datetime.now()
        update_time(window.start_time, time_label, window)

def stop_stopwatch(time_label, window):
    window.stop_timer = True
    now = datetime.datetime.now()
    elapsed_time = now - window.start_time
    minutes, seconds = divmod(elapsed_time.seconds, 60)
    game_time = f"{minutes}:{seconds:02d}"
    time_label.config(text=f"Game Time - {minutes}:{seconds:02d}")
    return game_time

def update_time(start_time, time_label, window):
    if window.stop_timer:
        return
    now = datetime.datetime.now()
    elapsed_time = now - start_time
    minutes, seconds = divmod(elapsed_time.seconds, 60)
    time_label.config(text=f"Game Time - {minutes}:{seconds:02d}")
    time_label.after(1000, update_time, start_time, time_label, window)

# Functions for game
def run_new_game():
    for widget in window.winfo_children():
        widget.destroy()
   
    # Reset game time
    window.stop_timer = False
    window.start_time = None 
    
    # Opening Text label
    gra_for = "-" * 64
    opening_text_label = ("Hi there!\n" + 
        gra_for + 
        "\nI've generated a random 4 digit number for you.\n"
        "Let's play Bulls and Cows game.\n" +
        gra_for +
        "\nGood Luck!"
    )
    text_label = tkinter.Label(window, text=opening_text_label, font=("Arial", 20), background="green", justify="left")
    text_label.place(x=10, y=10)
    
    # Entry label for guessing
    entry = tkinter.Entry(window, font=("Arial", 16), width=10)
    entry.place(x=1025, y=580)
    
    # Text for guessing label
    text_label_1 = tkinter.Label(window, text="Insert the number and press Enter button:", font=("Arial", 16), background="green")
    text_label_1.place(x=635, y=580)
    
    # Time label
    time_label = tkinter.Label(window, text="Game Time - 0:00", font=("Arial", 20), background="green", justify="right")
    time_label.place(x=820, y=10)
    
    # Register to display all previous guesses and results
    guesses_register = tkinter.Listbox(window, font=("Arial", 16), width=50, height=20)
    guesses_register.place(x=640, y=62)

    # Scrollbar for register
    scrollbar = tkinter.Scrollbar(window, orient="vertical", command=guesses_register.yview)
    guesses_register.config(yscrollcommand=scrollbar.set)
    scrollbar.place(x=1225, y=62, height=504)

    # Play game
    secret_number = generate_secret_number()
    guesses = 0
    
    def check_guess(event=None):
        nonlocal guesses
        guess = entry.get()
        
        # Guess validation
        is_valid, error_message = verify_guess(guess)
        if not is_valid:
            guesses_register.insert(tkinter.END, f"Invalid guess: {error_message}")
            guesses_register.yview_scroll(1, "units")
            return
        
        # first Enter - start stopwatch
        if window.start_time is None:
            start_stopwatch(time_label, window)
            
        guesses += 1
        guess_digits = [int(digit) for digit in guess]
        bulls, cows = evaluate_guess(secret_number, guess_digits)
        
        # register with results
        guesses_register.insert(tkinter.END, f"Guess {guesses}: {guess} >>> {bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        guesses_register.yview_scroll(1, "units")
        
        # showing results
        if bulls == 4:
            game_time = stop_stopwatch(time_label, window)
            guesses_register.insert(tkinter.END, f"Correct, you've guessed the right number in {guesses} guesses!\n")
            guesses_register.yview_scroll(1, "units")
            guesses_register.insert(tkinter.END, f"Your game time is {game_time}.\n")
            guesses_register.yview_scroll(1, "units")
            guesses_register.insert(tkinter.END, "That's amazing!")
            guesses_register.yview_scroll(1, "units")
            guesses_register.insert(tkinter.END, "Game over!")
            guesses_register.yview_scroll(1, "units")
            
            # Display New Game and End Game buttons after game ends
            new_game_button = tkinter.Button(window, text="New Game", font=("Arial", 20), width=15, height=2, command=run_new_game)
            new_game_button.place(x=200, y=300)
            
            end_game_button = tkinter.Button(window, text="End Game", font=("Arial", 20), width=15, height=2, command=end_game)
            end_game_button.place(x=200, y=400)
            
            stop_stopwatch(time_label, window)
            
        # Clear the entry after processing the guess
        entry.delete(0, tkinter.END)
    
    # Enter button - run game
    entry.bind("<Return>", check_guess)
    
    def end_game():
        window.quit()
        
# 1. GUI
# 1.1 Window
window = tkinter.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("Prepared by Roman Příhonský")
window.geometry(f"{screen_width}x{screen_height}")
window.configure(background="green")
window.start_time = None
window.stop_timer = False

# 1.2 Label
label = tkinter.Label(window, text="Welcome to BULLs & COWs game", font=("Arial", 40), background="green")
label.pack(pady=10)

# 1.3 button "NG"
button = tkinter.Button(window, text="NEW GAME", font=("Arial", 20), width=15, height=2, command=run_new_game)
button.place(x=525, y=200)

window.mainloop()
