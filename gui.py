import tkinter as tk

# Funkce pro zahájení hry
def start_game():
    # Zničení všech widgetů v hlavním okně
    for widget in window.winfo_children():
        widget.destroy()

    # Změna obsahu okna na hru
    window.configure(background="lightblue")
    game_label = tk.Label(window, text="BULLs & COWs - The Game", font=("Arial", 30), bg="lightblue")
    game_label.pack(pady=20)

    # Přidání instrukcí
    instruction_label = tk.Label(window, text="Try to guess the 4-digit number!", font=("Arial", 20), bg="lightblue")
    instruction_label.pack(pady=10)

    # Textové pole pro zobrazení historie (např. předchozí odhady)
    text_box = tk.Text(window, height=10, width=50, font=("Arial", 15))
    text_box.pack(pady=10)
    text_box.insert("1.0", "Game started! Enter your first guess below.\n")
    text_box.config(state="disabled")  # Znepřístupnění editace textu uživatelem

    # Vstupní pole pro uživatele
    guess_entry = tk.Entry(window, font=("Arial", 20), justify="center")
    guess_entry.pack(pady=10)

    # Funkce pro zpracování vstupu uživatele
    def submit_guess():
        guess = guess_entry.get()
        guess_entry.delete(0, tk.END)  # Vymazání vstupního pole
        # Aktualizace textového pole s historií
        text_box.config(state="normal")
        text_box.insert(tk.END, f"You guessed: {guess}\n")
        text_box.config(state="disabled")
        # Zde můžete přidat herní logiku pro kontrolu odhadu

    # Tlačítko pro odeslání odhadu
    submit_button = tk.Button(window, text="Submit Guess", font=("Arial", 20), command=submit_guess)
    submit_button.pack(pady=10)

    # Přidání tlačítka pro návrat do menu
    back_button = tk.Button(window, text="Back to Menu", font=("Arial", 20), command=show_main_menu)
    back_button.pack(pady=20)

# Funkce pro zobrazení hlavního menu
def show_main_menu():
    # Zničení všech widgetů v hlavním okně
    for widget in window.winfo_children():
        widget.destroy()

    # Obnovení hlavního menu
    window.configure(background="green")
    label = tk.Label(window, text="Welcome to BULLs & COWs game", font=("Arial", 40), background="green")
    label.pack(pady=10)

    button_new_game = tk.Button(window, text="NEW GAME", font=("Arial", 20), width=15, height=2, command=start_game)
    button_new_game.place(x=525, y=200)

    button_statistics = tk.Button(window, text="GAME STATISTICS", font=("Arial", 20), width=15, height=2)
    button_statistics.place(x=525, y=350)

    button_options = tk.Button(window, text="OPTIONS", font=("Arial", 20), width=15, height=2)
    button_options.place(x=525, y=500)

# Hlavní okno
window = tk.Tk()
window.title("Prepared by Roman Příhonský")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.configure(background="green")

# Zobrazení hlavního menu
show_main_menu()

# Spuštění smyčky
window.mainloop()
