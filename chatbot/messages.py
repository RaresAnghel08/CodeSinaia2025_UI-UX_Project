import tkinter as tk
from chatbot.probability import get_response
from ux.alerts import empty_message_alert, save_success_alert, load_success_alert, clear_success_alert, error_alert, file_not_found_alert
def send_message(entry, chat_log):
    
    #TODO: check and alert in a separate windows if empty message
    if not entry.get():
        empty_message_alert()
        return

    user_message = entry.get()
    if user_message.strip() == "":
        empty_message_alert()
        return

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_message.strip()}\n")
    
    bot_response = get_response(user_message)
    chat_log.insert(tk.END, f"Bot: {bot_response}\n\n")
    chat_log.see("end")
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    
def clear_chat(chat_log):
    chat_log.config(state=tk.NORMAL)
    chat_log.delete('1.0', tk.END)
    chat_log.config(state=tk.DISABLED)
    clear_success_alert()
    
