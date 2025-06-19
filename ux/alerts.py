import tkinter as tk
import os

ASSETS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")


def center_window(window, width=300, height=100):
    # TODO: Center the window on the screen
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    
    # window.iconbitmap(os.path.join(ASSETS_PATH, "code_sinaia_logo.ico")) #there is no ico file
    # Set the icon for the window as png
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file=os.path.join(ASSETS_PATH, "code_sinaia_logo.png")))

def empty_message_alert():
    alert = tk.Toplevel()
    alert.title("Alert")
    alert.configure(bg="#ff0015")
    center_window(alert)
    alert_label = tk.Label(alert, text="Please enter a message.", bg="#f8d7da", fg="#ff0019", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#f5c6cb", fg="#ff0019")
    ok_button.pack(pady=10)

def save_success_alert():
    alert = tk.Toplevel()
    alert.title("Success")
    alert.configure(bg="#d4edda")
    center_window(alert)
    alert_label = tk.Label(alert, text="History saved successfully.", bg="#d4edda", fg="#155724", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#c3e6cb", fg="#155724")
    ok_button.pack(pady=10)
    
def load_success_alert():
    alert = tk.Toplevel()
    alert.title("Success")
    alert.configure(bg="#d4edda")
    center_window(alert)
    alert_label = tk.Label(alert, text="History loaded successfully.", bg="#d4edda", fg="#155724", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#c3e6cb", fg="#155724")
    ok_button.pack(pady=10)

def clear_success_alert():
    alert = tk.Toplevel()
    alert.title("Success")
    alert.configure(bg="#d4edda")
    center_window(alert)
    alert_label = tk.Label(alert, text="Chat cleared successfully.", bg="#d4edda", fg="#155724", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#c3e6cb", fg="#155724")
    ok_button.pack(pady=10)
    
def error_alert(message):
    alert = tk.Toplevel()
    alert.title("Error")
    alert.configure(bg="#f8d7da")
    center_window(alert)
    alert_label = tk.Label(alert, text=message, bg="#f8d7da", fg="#721c24", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#f5c6cb", fg="#721c24")
    ok_button.pack(pady=10)
    
def file_not_found_alert():
    alert = tk.Toplevel()
    alert.title("Error")
    alert.configure(bg="#f8d7da")
    center_window(alert)
    alert_label = tk.Label(alert, text="File not found.", bg="#f8d7da", fg="#721c24", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#f5c6cb", fg="#721c24")
    ok_button.pack(pady=10)

def json_decode_error_alert():
    alert = tk.Toplevel()
    alert.title("Error")
    alert.configure(bg="#f8d7da")
    center_window(alert)
    alert_label = tk.Label(alert, text="Error decoding JSON.", bg="#f8d7da", fg="#721c24", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#f5c6cb", fg="#721c24")
    ok_button.pack(pady=10)

def no_history_alert():
    alert = tk.Toplevel()
    alert.title("Alert")
    alert.configure(bg="#ff0015")
    center_window(alert)
    alert_label = tk.Label(alert, text="No chat history found.", bg="#f8d7da", fg="#ff0019", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#f5c6cb", fg="#ff0019")
    ok_button.pack(pady=10)