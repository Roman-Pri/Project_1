import random

def generate_secret_number():
    """Generuje tajné 4místné číslo s unikátními číslicemi, bez nuly na začátku."""
    digits = random.sample(range(1, 10), 4)  # 4 unikátní číslice od 1 do 9
    return ''.join(map(str, digits))

def validate_input(user_input):
    """Validace vstupu uživatele."""
    if len(user_input) != 4:
        return "Číslo musí být přesně 4místné."
    if not user_input.isdigit():  # Kontrola, že vstup obsahuje jen číslice
        return "Číslo může obsahovat pouze číslice."
    if user_input[0] == '0':
        return "Číslo nesmí začínat nulou."
    if len(set(user_input)) != 4:
        return "Číslo nesmí obsahovat duplicity."
    return None  # Pokud je vstup validní

def count_bulls_cows(secret, guess):
    """Vyhodnocení tipu hráče."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(s in guess for s in secret) - bulls
    return bulls, cows

def play_game():
    secret_number = generate_secret_number()
    print(f"Tajné číslo: {secret_number}")  # Pro kontrolu během testování
    attempts = 0
    
    while True:
        user_input = input("Zadej své 4místné číslo: ")
        validation_result = validate_input(user_input)
        
        if validation_result:  # Pokud neprojde validací
            print(validation_result)
        else:
            attempts += 1
            bulls, cows = count_bulls_cows(secret_number, user_input)
            
            if bulls == 4:  # Uživatel uhodl tajné číslo
                print(f"Gratuluji! Uhodl jsi číslo za {attempts} pokusů.")
                break
            
            # Výstup podle počtu bulls a cows
            bull_word = "bull" if bulls == 1 else "bulls"
            cow_word = "cow" if cows == 1 else "cows"
            print(f"{bulls} {bull_word} a {cows} {cow_word}")
