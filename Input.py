import tkinter as tk
from tkinter import messagebox
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x500")

        # Use a unique font
        self.custom_font = ("Courier New", 16)

        # Welcome screen
        self.welcome_label = tk.Label(
            root, text="Welcome to this typing test!", font=("Courier New", 24, "bold")
        )
        self.welcome_label.pack(pady=50)

        self.start_button = tk.Button(
            root, text="Start", command=self.start_test, font=self.custom_font
        )
        self.start_button.pack(pady=20)

        # Sample text and typing area (hidden initially)
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.sample_display = tk.Text(
            root, height=5, width=60, font=self.custom_font, wrap="word", state=tk.DISABLED
        )
        self.entry = tk.Text(root, height=10, width=60, font=self.custom_font)
        self.reset_button = tk.Button(
            root, text="Reset", command=self.reset_test, font=self.custom_font
        )

        self.start_time = None
        self.end_time = None

    def start_test(self):
        # Hide welcome screen and show typing test
        self.welcome_label.pack_forget()
        self.start_button.pack_forget()

        # Show sample text and typing area
        self.sample_display.pack(pady=10)
        self.entry.pack(pady=10)
        self.reset_button.pack(pady=10)

        # Initialize the test
        self.sample_display.config(state=tk.NORMAL)
        self.sample_display.delete(1.0, tk.END)
        self.sample_display.insert(tk.END, self.sample_text)
        self.sample_display.config(state=tk.DISABLED)

        self.entry.config(state=tk.NORMAL)
        self.entry.delete(1.0, tk.END)
        self.entry.focus()

        self.start_time = time.time()
        self.entry.bind("<KeyRelease>", self.check_typing)

    def check_typing(self, event):
        typed_text = self.entry.get(1.0, tk.END).strip()
        self.highlight_text()  # Update highlighting as the user types

        if typed_text == self.sample_text:
            self.end_time = time.time()
            self.calculate_speed()
            self.entry.config(state=tk.DISABLED)

    def highlight_text(self):
        typed_text = self.entry.get(1.0, tk.END).strip()
        self.sample_display.config(state=tk.NORMAL)
        self.sample_display.delete(1.0, tk.END)

        for i in range(len(typed_text)):
            if i < len(self.sample_text):
                if typed_text[i] == self.sample_text[i]:
                    # Correct letter: blue
                    self.sample_display.insert(tk.END, self.sample_text[i], "correct")
                else:
                    # Incorrect letter: red
                    self.sample_display.insert(tk.END, self.sample_text[i], "incorrect")
            else:
                # Extra letters: red
                self.sample_display.insert(tk.END, self.sample_text[i], "incorrect")

        # Add remaining sample text as default color
        if len(typed_text) < len(self.sample_text):
            self.sample_display.insert(tk.END, self.sample_text[len(typed_text):])

        self.sample_display.config(state=tk.DISABLED)

        # Configure tags for colors
        self.sample_display.tag_config("correct", foreground="blue")
        self.sample_display.tag_config("incorrect", foreground="red")

    def calculate_speed(self):
        time_taken = self.end_time - self.start_time
        words = len(self.sample_text.split())
        wpm = (words / time_taken) * 60
        messagebox.showinfo("Typing Speed", f"Your typing speed is: {wpm:.2f} WPM")

    def reset_test(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(1.0, tk.END)
        self.start_time = None
        self.end_time = None
        self.highlight_text()  # Reset highlighting

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()