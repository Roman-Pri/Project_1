import random
import datetime
import tkinter as tk

# Globální proměnné
start_time = None
target_number = None  # Náhodné číslo k uhodnutí

# Funkce pro aktualizaci času
def update_time(time_label):
    """Aktualizuje stopky na obrazovce."""
    if start_time:
        now = datetime.datetime.now()
        elapsed_time = now - start_time
        minutes, seconds = divmod(elapsed_time.seconds, 60)
        time_label.config(text=f"Game Time - {minutes}:{seconds:02d}")
        time_label.after(1000, update_time, time_label)  # Aktualizace každou sekundu

def on_enter(event, entry, time_label, result_label):
    """Spustí stopky při prvním zadání čísla a zkontroluje odpověď."""
    global start_time
    guess = entry.get()

    if not guess.isdigit() or len(guess) != 4:  # Kontrola platného vstupu
        result_label.config(text="Please enter a 4-digit number!", fg="red")
        return
    
    if start_time is None:  # Spustíme stopky při prvním zadání čísla
        start_time = datetime.datetime.now()
        update_time(time_label)

    if guess == target_number:  # Pokud hráč uhodne správně
        stop_time = datetime.datetime.now()
        elapsed_time = stop_time - start_time
        minutes, seconds = divmod(elapsed_time.seconds, 60)
        result_label.config(text=f"🎉 Correct! Time: {minutes}:{seconds:02d} 🎉", fg="blue")
        entry.config(state="disabled")  # Zakáže další zadávání čísel
        time_label.after_cancel(update_time)  # Zastaví aktualizaci času
    else:
        result_label.config(text="Wrong guess! Try again.", fg="black")

def run_new_game():
    """Inicializuje novou hru a resetuje stopky."""
    global start_time, target_number
    start_time = None  # Reset času
    target_number = str(random.randint(1000, 9999))  # Generujeme nové číslo
    print(f"Debug: Target number is {target_number}")  # Pro testování

    for widget in window.winfo_children():
        widget.destroy()
    
    # Úvodní text
    opening_text = "Hi there!\nI've generated a random 4-digit number for you.\nLet's play Bulls and Cows game.\nInsert the number and press Enter:"
    label = tk.Label(window, text=opening_text, font=("Arial", 20), background="green", justify="left")
    label.place(x=10, y=10)

    # Vstupní pole
    entry = tk.Entry(window, font=("Arial", 16), width=10)
    entry.place(x=10, y=220)

    # Časový ukazatel
    time_label = tk.Label(window, text="Game Time - 0:00", font=("Arial", 30), background="green", justify="right")
    time_label.place(x=940, y=10)

    # Výsledek pokusu
    result_label = tk.Label(window, text="", font=("Arial", 20), background="green")
    result_label.place(x=10, y=300)

    # Připojení funkce na stisk Enteru
    entry.bind("<Return>", lambda event: on_enter(event, entry, time_label, result_label))

# Vytvoření hlavního okna
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("Prepared by Roman Příhonský")
window.geometry(f"{screen_width}x{screen_height}")
window.configure(background="green")

# Hlavní menu
label = tk.Label(window, text="Welcome to BULLs & COWs game", font=("Arial", 40), background="green")
label.pack(pady=10)

# Tlačítko "NEW GAME"
button = tk.Button(window, text="NEW GAME", font=("Arial", 20), width=15, height=2, command=run_new_game)
button.place(x=525, y=200)

# Tlačítka bez funkce (zatím)
button = tk.Button(window, text="GAME STATISTICS", font=("Arial", 20), width=15, height=2)
button.place(x=525, y=350)

button = tk.Button(window, text="OPTIONS", font=("Arial", 20), width=15, height=2)
button.place(x=525, y=500)

window.mainloop()