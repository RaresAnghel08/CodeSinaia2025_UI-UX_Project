from hints import hints

#print welcome message
print("Bine ai venit la chatbot! Aici poți obține indicii pentru a-ți îmbunătăți codul.")
user_input = input("De care hint ai nevoie: ").lower()

# check if the user input matches any predefined hint
if user_input in hints:
    print(hints[user_input])
else:
    print("Nu am un hint pentru asta. Te rog să reîncerci.")