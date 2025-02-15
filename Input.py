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

        # Use a Text widget to display the sample text with colored formatting
        self.sample_display = tk.Text(root, height=5, width=50, font=("Arial", 12), wrap="word")
        self.sample_display.insert(tk.END, self.sample_text)
        self.sample_display.config(state=tk.DISABLED)  # Make it read-only
        self.sample_display.pack(pady=10)

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
        self.highlight_text()  # Reset highlighting when starting

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
        self.start_button.config(state=tk.NORMAL)
        self.start_time = None
        self.end_time = None
        self.highlight_text()  # Reset highlighting

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()