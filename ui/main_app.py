import tkinter as tk
from chatbot.messages import send_message, clear_chat

def open_app():
    root = tk.Tk()
    root.title("Chatbot")
    
    #TODO
    # #upper left image logo
    # root.iconbitmap('logo.ico')  # Ensure you have a logo.ico file in the same directory
    
    window_width = 500
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    splash_x = (screen_width // 2) - (window_width // 2)
    splash_y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{splash_x}+{splash_y}")

    chat_log = tk.Text(root, state=tk.DISABLED, wrap="word")
    chat_log.pack(padx=10, pady=10, expand=True, fill='both')
    # TODO: load data.json
    with open("data.json", "r") as f:
        data = f.read()
        chat_log.insert(tk.END, data)
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
    
    
    root.bind('<Return>', lambda event=None: send_message(entry, chat_log))

    root.mainloop()


