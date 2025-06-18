import tkinter as tk
from chatbot.messages import send_message, clear_chat
import json
from tkinter import messagebox

def load_chat(chat_log):
    try:
        with open("data/data.json", "r", encoding="utf-8") as f:
            messages = json.load(f)
        if not messages:
            messagebox.showinfo("Istoric gol", "Istoricul este gol.")
            return
        chat_log.config(state=tk.NORMAL)
        chat_log.delete("1.0", tk.END)
        for msg in messages:
            chat_log.insert(tk.END, f"{msg['sender']}: {msg['text']}\n")
        chat_log.config(state=tk.DISABLED)
    except FileNotFoundError:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "Fisierul 'data.json' nu a fost găsit.\n")
        # create the file if it doesn't exist
        with open("data/data.json", "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        chat_log.insert(tk.END, "Un fișier nou a fost creat.\n")
        chat_log.insert(tk.END, "Încercați din nou să încărcați istoricul.\n")
        chat_log.insert(tk.END, "Dacă problema persistă, verificați permisiunile fișierului.\n")
        chat_log.config(state=tk.DISABLED)
    except json.JSONDecodeError:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "Eroare la citirea fișierului JSON.\n")
        chat_log.config(state=tk.DISABLED)
        
def save_chat(chat_log):
    lines = chat_log.get("1.0", tk.END).strip().split("\n")
    messages = []

    for line in lines:
        if ": " in line:
            sender, text = line.split(": ", 1)
            messages.append({"sender": sender, "text": text})

    with open("data/data.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)
        
def open_app():
    root = tk.Tk()
    root.title("Chatbot")
    
    #TODO
    # #upper left image logo
    # root.iconbitmap('logo.ico')  # Ensure you have a logo.ico file in the same directory
    
    window_width = 600
    window_height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    splash_x = (screen_width // 2) - (window_width // 2)
    splash_y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{splash_x}+{splash_y}")

    chat_log = tk.Text(root, state=tk.DISABLED, wrap="word", bg="#D9D9D9")
    chat_log.pack(padx=10, pady=10, expand=True, fill='both')
    # TODO: load data.json
    # with open("data.json", "r") as f:
    #     data = f.read()
    #     chat_log.insert(tk.END, data)
    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=5)

    entry = tk.Entry(entry_frame, width=50)
    entry.pack(side=tk.LEFT, padx=(0, 10))

    # TODO:fa un buton in figma pt a trimite textul / & sterge chatul la care sa ii pui bacground imaginea si action
    # button_image_input = PhotoImage(file=relative_to_assets("button_input.png"))
    # Button_input = Button(
    #     image=button_image_input,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=select_input_folder,
    #     relief="flat",
    #     activebackground="#D9D9D9",
    #     background="#D9D9D9"
    # )
    send_button = tk.Button(entry_frame, text="Trimite", command=lambda: send_message(entry, chat_log))
    send_button.pack(side=tk.LEFT)
    
    # TODO: optional - sa puna si place la buton
    # Button_input.place(
    #     x=22.0,
    #     y=84.0,
    #     width=755.0,
    #     height=56.0
    # )

    clear_button = tk.Button(entry_frame, text="Clear Chat", command=lambda: clear_chat(chat_log))
    clear_button.pack(side=tk.LEFT, padx=(10, 0))

    #TODO: alerta daca chatul deja e gol
    
    button_frame = tk.Frame(root)
    button_frame.pack(pady=(5, 10))

    load_button = tk.Button(button_frame, text="Load Chat", command=lambda: load_chat(chat_log))
    load_button.pack(side=tk.LEFT, padx=5)

    save_button = tk.Button(button_frame, text="Save Chat", command=lambda: save_chat(chat_log))
    save_button.pack(side=tk.LEFT, padx=5)
    
    root.bind('<Return>', lambda event=None: send_message(entry, chat_log))

    root.mainloop()


