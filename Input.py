import tkinter as tk
from tkinter import messagebox
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.start_time = None
        self.end_time = None

        self.label = tk.Label(root, text="Type the following text:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.sample_label = tk.Label(root, text=self.sample_text, font=("Arial", 12), wraplength=500)
        self.sample_label.pack(pady=10)

        self.entry = tk.Text(root, height=10, width=50, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.check_typing)

        self.start_button = tk.Button(root, text="Start", command=self.start_test, font=("Arial", 12))
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_test, font=("Arial", 12))
        self.reset_button.pack(pady=10)

    def start_test(self):
        self.start_time = time.time()
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(1.0, tk.END)
        self.start_button.config(state=tk.DISABLED)

    def check_typing(self, event):
        typed_text = self.entry.get(1.0, tk.END).strip()
        if typed_text == self.sample_text:
            self.end_time = time.time()
            self.calculate_speed()
            self.entry.config(state=tk.DISABLED)

    def calculate_speed(self):
        time_taken = self.end_time - self.start_time
        words = len(self.sample_text.split())
        wpm = (words / time_taken) * 60
        messagebox.showinfo("Typing Speed", f"Your typing speed is: {wpm:.2f} WPM")

    def reset_test(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(1.0, tk.END)
        self.start_button.config(state=tk.NORMAL)
        self.start_time = None
        self.end_time = None

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()