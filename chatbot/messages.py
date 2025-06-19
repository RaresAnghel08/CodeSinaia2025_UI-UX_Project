import tkinter as tk
from chatbot.probability import get_response

def send_message(entry, chat_log):
    
    #TODO: check and alert in a separate windows if empty message
    if not entry.get():
        # de customizat
        '''
        de centrat
        de scos butonul de ok
        de pus un mesaj de genul "Please enter a message."
        ceva cu semnul ala rosu de eroare
        de pus un icon de eroare
        de pus un background la fereastra de alert
        de pus un titlu la fereastra de alert
        '''
        #TODO: de revizuit
        alert = tk.Toplevel()
        alert.title("Alert")
        alert.geometry("300x100")
        alert.configure(bg="#ff0015")
        # alert.iconbitmap('error.ico')  # Ensure you have an error.ico file in the same directory
        alert_label = tk.Label(alert, text="Please enter a message.", bg="#f8d7da", fg="#ff0019", font=("Helvetica", 12))
        alert_label.pack(expand=True)
        ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#f5c6cb", fg="#ff0019")
        ok_button.pack(pady=10)
        return
    
    user_message = entry.get()
    if user_message.strip() == "":
        return

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_message}\n")
    
    bot_response = get_response(user_message)
    chat_log.insert(tk.END, f"Bot: {bot_response}\n\n")
    
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    
def clear_chat(chat_log):
    chat_log.config(state=tk.NORMAL)
    chat_log.delete('1.0', tk.END)
    chat_log.config(state=tk.DISABLED)
    
