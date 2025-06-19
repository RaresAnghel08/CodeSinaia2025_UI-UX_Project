import json
import tkinter as tk
from tkinter import messagebox


def load_chat(chat_log):
    try:
        with open("data/history.json", "r", encoding="utf-8") as f:
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
        chat_log.insert(tk.END, "Fisierul 'data/history.json' nu a fost găsit.\n")
        with open("data/history.json", "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        chat_log.insert(tk.END, "Un fișier nou a fost creat.\n")
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
    with open("data/history.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)