"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Ing. Roman Příhonský, MMS, MSS
email:  roman.prihonsky83@gmail.com
"""
import random           # podpora pro tvorbu nahodneho cisla
import datetime         # podpora pro mereni delky hry
import tkinter          # GUI
import pandas           # uchovani statistik
import matplotlib       # zobrazeni statistik

# Functions definition
def generate_secret_number():
    while True:
        secret_number = "".join(random.sample("1234567890", 4))
        if secret_number[0] != "0":
            return secret_number

def evaluate_guess(secret_number, guess):
    bulls = sum([1 for i in range(4) if secret_number[i] == guess[i]])
    cows = sum([1 for i in range(4) if guess[i] in secret_number and secret_number[i] != guess[i]])
    return bulls, cows

def validate_guess(guess):
    if len(guess) != 4:
        return False, "Your guess must be exactly 4 digits."
    if not guess.isdigit():
        return False, "Your guess must contain only digits."
    if len(set(guess)) != len(guess):
        return False, "Your guess must not contain duplicate digits."
    if guess[0] == '0':
        return False, "Your guess must not start with 0."
    return True, ""

def update_time(start_time, time_label, window):
    if window.stop_timer:  # Check if timer should stop
        return
    now = datetime.datetime.now()
    elapsed_time = now - start_time
    minutes, seconds = divmod(elapsed_time.seconds, 60)
    time_label.config(text=f"Game Time - {minutes}:{seconds:02d}")
    time_label.after(1000, update_time, start_time, time_label, window)

def start_stopwatch(time_label, window):
    if window.start_time is None:
        window.start_time = datetime.datetime.now()
        update_time(window.start_time, time_label, window)

def stop_stopwatch(time_label, window):
    window.stop_timer = True  # Stop the timer when the game ends
    now = datetime.datetime.now()
    elapsed_time = now - window.start_time
    minutes, seconds = divmod(elapsed_time.seconds, 60)
    time_label.config(text=f"Game Time - {minutes}:{seconds:02d}")  # Display final time

def run_new_game():
    for widget in window.winfo_children():
        widget.destroy()
   
    # Reset game time
    window.stop_timer = False  # Allow the timer to run again
    
    # Game time
    window.start_time = None
    
    # Opening label
    gra_for = "-" * 64
    opening_text_label = ("Hi there!\n" + 
        gra_for + 
        "\nI've generated a random 4 digit number for you.\n"
        "Let's play Bulls and Cows game.\n" +
        gra_for +
        "\nInsert the number and press Enter button:"
    )
    label = tkinter.Label(window, text = opening_text_label, font = ("Arial", 20), background = "green", justify = "left")
    label.place(x = 10, y = 10)
    
    # Entry label for guessing
    entry = tkinter.Entry(window, font = ("Arial", 16), width = 10, )
    entry.place(x = 10, y = 220)
    
    # Time label
    time_label = tkinter.Label(window, text="Game Time - 0:00", font=("Arial", 30), background = "green", justify = "right")
    time_label.place(x = 940, y = 10)
    
    # Listbox to display all previous guesses and results
    guesses_listbox = tkinter.Listbox(window, font=("Arial", 14), width=50, height=10)
    guesses_listbox.place(x = 10, y = 300)

    # Play game
    secret_number = generate_secret_number()
    guesses = 0
    def check_guess():
        nonlocal guesses
        guess = entry.get()
        
        # Guess validation
        is_valid, error_message = validate_guess(guess)
        if not is_valid:
            label.config(text=error_message)
            return
        
        guesses += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        
        # Add guess to the listbox with results
        guesses_listbox.insert(tkinter.END, f"Guess {guesses}: {guess} -> {bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        
        # showing results
        if bulls == 4:
            label.config(text=f"Correct, you've guessed the right number in {guesses} guesses!\nGame Over!")
            stop_stopwatch(time_label, window)  # Stop timer when game ends
        else:
            label.config(text=f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
    
    def start_on_submit():
        start_stopwatch(time_label, window)
        check_guess()
        
    # Submit guess button
    submit_button = tkinter.Button(window, text="Submit Guess", font=("Arial", 16), command=start_on_submit)
    submit_button.place(x=10, y=250)

# Function to restart the game
def restart_game():
    run_new_game()  # Call the function that resets everything and starts a new game

# 1.GUI
# 1.1 Window
window = tkinter.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("Prepared by Roman Příhonský")
window.geometry(f"{screen_width}x{screen_height}")
window.configure(background = "green") 
window.stop_timer = False

# 1.2 Label
label = tkinter.Label(window, text = "Welcome to BULLs & COWs game", font = ("Arial", 40), background = "green")
label.pack(pady = 10)

# 1.3 button "NG"
button = tkinter.Button(window, text = "NEW GAME", font = ("Arial", 20), width = 15, height = 2, command = run_new_game) 
button.place(x = 525, y = 200)

# 1.4 button "GS"
button = tkinter.Button(window, text = "GAME STATISTICS", font = ("Arial", 20), width = 15, height= 2) # Missing command for button
button.place(x = 525, y = 350)

# 1.5 button "Opt"
button = tkinter.Button(window, text = "OPTIONS", font = ("Arial", 20), width = 15, height= 2) # Missing command for button
button.place(x = 525, y = 500)

# 1.6 button "Restart Game"
restart_button = tkinter.Button(window, text = "RESTART GAME", font = ("Arial", 20), width = 15, height = 2, command = restart_game)
restart_button.place(x = 525, y = 650)

window.mainloop()
