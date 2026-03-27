def add_setting(settings, key_value_pair):

	key = key_value_pair[0].lower()
	value = key_value_pair[1].lower()

	if key in settings:
		return f"Setting '{key}' already exists! Cannot add a new setting with this name."


	settings[key] = value
	return f"Setting '{key}' added with value '{value}' successfully!"



def update_setting(settings, key_value_pair):

	key = key_value_pair[0].lower()
	value = key_value_pair[1].lower()
	
	if not key in settings:
		return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

	settings[key] = value
	return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key_setting):
	
	key = key_setting.lower()

	if key in settings:
		del settings[key]
		return f"Setting '{key}' deleted successfully!"
		
	return "Setting not found!"
		

	
	


def view_settings(settings):
	
	if not settings:
		return "No settings available."

	output = "Current User Settings:"

	for key, value in settings.items():
		output += f"\n{key.capitalize()}: {value}"
	return output + "\n"


def start_app():
    # 1. Vytvoríš prázdny slovník pre aplikáciu
    moje_data = {}

    while True:
        print("\n--- MOJA APPKA ---")
        print("1. Pridať | 2. Update | 3. Zmazať | 4. Vidieť | 5. Koniec")
        volba = input("Vyber si číslo: ")

        if volba == "1":
            k = input("Zadaj kľúč: ")
            v = input("Zadaj hodnotu: ")
            # TU obalíš volanie funkcie do printu:
            print(add_setting(moje_data, (k, v)))

        elif volba == "2":
            k = input("Zadaj kľúč: ")
            v = input("Zadaj hodnotu: ")
            # TU obalíš volanie funkcie do printu:
            print(update_setting(moje_data, (k, v)))

        elif volba == "3":
            k = input("Zadaj kľúč: ")
     
            # TU obalíš volanie funkcie do printu:
            print(delete_setting(moje_data, (k)))


        elif volba == "4":
            # TU uvidíš ten zoznam s Capitalize a novými riadkami:
            print(view_settings(moje_data))

        elif volba == "5":
            print("Čau!")
            break

# 3. Spustenie aplikácie
if __name__ == "__main__":
    start_app()





	

	










# --- TESTOVANIE ---

# # 1. Vytvor si prázdny slovník
# moje_nastavenia = {}

# # 2. Skús pridať prvé nastavenie
# vysledok1 = add_setting(moje_nastavenia, ("Theme", "Dark"))
# print(vysledok1)  # Malo by vypísať: Setting 'theme' added...

# # 3. Skús pridať TO ISTÉ nastavenie znova (test chyby)
# vysledok2 = add_setting(moje_nastavenia, ("THEME", "Light"))
# print(vysledok2)  # Malo by vypísať: Setting 'theme' already exists!

# # 4. Pozri sa, ako vyzerá slovník teraz
# print(f"Aktuálny slovník: {moje_nastavenia}")

# vysledok3 = add_setting(moje_nastavenia, ('meno', 'Michal'))
# print(f"Aktuálny slovník: {moje_nastavenia}")

# vysledok4 = add_setting(moje_nastavenia, ('meno', 'Stevka'))
# print(vysledok4)

# vysledok5 = add_setting(moje_nastavenia, ('meno', 'STEVKA'))
# print(vysledok5)

# print(f"Aktuálny slovník: {moje_nastavenia}")




# def add_settings():
	
# 	while True:
# 		name = input("zadaj meno: ")
# 		if name.isalpha():
# 			break
# 		print("Chyba: Vstup nesmie obsahovať čísla ani špeciálne znaky!")

# 	while True:
# 		surname = input("zadaj priezvisko: ")
# 		if surname.isalpha():
# 			break
# 		print("Chyba: Vstup nesmie obsahovať čísla ani špeciálne znaky!")

# 	while True:
# 		vek = input("zadaj vek: ")
# 		if vek.isdigit():
# 			break
# 		print("Chyba: Vstup nesmie obsahovať slova, len cisla!")
	

# 	person = {
# 		'name': name,
# 		'surname': surname,
# 		'vek': vek
# 	}

# 	print(person.values())



# --- 1. TU DAJ SVOJE FUNKCIE (Zadanie FreeCodeCamp) ---

# def add_setting(settings, key_value_pair):
#     # tvoj kód...
#     pass

# def update_setting(settings, key_value_pair):
#     # tvoj kód...
#     pass

# def delete_setting(settings, key):
#     # tvoj kód...
#     pass

# def view_settings(settings):
#     # tvoj kód...
#     pass

# # --- 2. TU VYTVOR PRÁZDNY SLOVNÍK ---
# test_settings = {}

# # --- 3. TU DAJ TÚ INTERAKTÍVNU ČASŤ (Aplikáciu) ---

# def start_app():
#     # Použijeme ten náš test_settings, ktorý sme vytvorili vyššie
#     while True:
#         print("\n--- MENU ---")
#         print("1. Pridať | 2. Update | 3. Zmazať | 4. Vidieť všetko | 5. Koniec")
        
#         volba = input("Vyber si (1-5): ")
        
#         if volba == "1":
#             k = input("Názov: ")
#             v = input("Hodnota: ")
#             print(add_setting(test_settings, (k, v)))
            
#         elif volba == "2":
#             k = input("Čo zmeniť: ")
#             v = input("Nová hodnota: ")
#             print(update_setting(test_settings, (k, v)))
            
#         elif volba == "3":
#             k = input("Čo zmazať: ")
#             print(delete_setting(test_settings, k))
            
#         elif volba == "4":
#             print(view_settings(test_settings))
            
#         elif volba == "5":
#             break

# # --- 4. SPUSTENIE ---
# if __name__ == "__main__":
#     start_app()





	
	

	


	
	

	
	
	
	
	

	
	


