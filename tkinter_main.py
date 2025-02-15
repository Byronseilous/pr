import tkinter as tk
from tkinter import messagebox
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.attributes("-fullscreen", True)  # Make the window fullscreen
        self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen", False))  # Exit fullscreen on Escape

        # Define a modern color palette
        self.COLORS = {
            "background": "#2E3440",  # Dark gray
            "text": "#D8DEE9",        # Light gray
            "button": "#5E81AC",       # Blue
            "highlight": "#88C0D0",    # Light blue
            "error": "#BF616A",        # Red
            "success": "#A3BE8C",      # Green
        }

        # Set background color
        self.root.config(bg=self.COLORS["background"])

        # Welcome screen
        self.welcome_label = tk.Label(
            root, text="Welcome to this typing test!", font=("Courier New", 24, "bold"),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.welcome_label.pack(pady=50)

        # Start button
        self.start_button = tk.Button(
            root, text="Start", command=self.start_test, font=("Courier New", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat"
        )
        self.start_button.pack(pady=20)

        # Sample text and typing area (hidden initially)
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.sample_display = tk.Text(
            root, height=5, width=60, font=("Courier New", 16), wrap="word", state=tk.DISABLED,
            bg=self.COLORS["background"], fg=self.COLORS["text"]
        )
        self.entry = tk.Text(
            root, height=10, width=60, font=("Courier New", 16),
            bg=self.COLORS["background"], fg=self.COLORS["text"], insertbackground=self.COLORS["text"]
        )
        self.reset_button = tk.Button(
            root, text="Reset", command=self.reset_test, font=("Courier New", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat"
        )

        # Add 30 buttons for future functionality
        self.button_frame = tk.Frame(root, bg=self.COLORS["background"])
       # self.create_buttons()

        self.start_time = None
        self.end_time = None

    # def create_buttons(self):
    #     """Create 30 buttons in a 5x6 grid."""
    #     for i in range(30):
    #         row = i // 6  # 6 buttons per row
    #         col = i % 6    # 6 columns
    #         button = tk.Button(
    #             self.button_frame,
    #             text=f"Button {i+1}",
    #             command=lambda i=i: self.button_click(i + 1),
    #             bg=self.COLORS["button"], fg=self.COLORS["text"], font=("Arial", 12), relief="flat"
    #         )
    #         button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    #
    #     # Configure grid weights to make buttons expand evenly
    #     for r in range(5):
    #         self.button_frame.grid_rowconfigure(r, weight=1)
    #     for c in range(6):
    #         self.button_frame.grid_columnconfigure(c, weight=1)
    #
    # def button_click(self, button_number):
    #     """Placeholder function for button clicks."""
    #     print(f"Button {button_number} clicked!")  # Replace with actual functionality

    def start_test(self):
        """Start the typing test."""
        self.welcome_label.pack_forget()
        self.start_button.pack_forget()

        # Show sample text and typing area
        self.sample_display.pack(pady=10)
        self.entry.pack(pady=10)
        self.reset_button.pack(pady=10)
        self.button_frame.pack(fill="both", expand=True)

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
        """Check the user's typing and update the UI."""
        typed_text = self.entry.get(1.0, tk.END).strip()
        self.highlight_text()

        # Check if the user has finished typing
        if len(typed_text) >= len(self.sample_text):
            self.end_time = time.time()
            self.calculate_speed_and_accuracy(typed_text)

    def highlight_text(self):
        """Highlight the sample text based on user input."""
        typed_text = self.entry.get(1.0, tk.END).strip()
        self.sample_display.config(state=tk.NORMAL)
        self.sample_display.delete(1.0, tk.END)

        for i in range(len(typed_text)):
            if i < len(self.sample_text):
                if typed_text[i] == self.sample_text[i]:
                    # Correct letter: green
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
        self.sample_display.tag_config("correct", foreground=self.COLORS["success"])
        self.sample_display.tag_config("incorrect", foreground=self.COLORS["error"])

    def calculate_speed_and_accuracy(self, typed_text):
        """Calculate and display typing speed and accuracy."""
        time_taken = self.end_time - self.start_time

        # Calculate typing speed (WPM)
        words = len(self.sample_text.split())
        wpm = (words / time_taken) * 60

        # Calculate accuracy
        correct_chars = 0
        for i in range(min(len(typed_text), len(self.sample_text))):
            if typed_text[i] == self.sample_text[i]:
                correct_chars += 1

        total_chars = len(self.sample_text)
        accuracy = (correct_chars / total_chars) * 100

        # Display results
        messagebox.showinfo(
            "Typing Results",
            f"Your typing speed is: {wpm:.2f} WPM\n"
            f"Your accuracy is: {accuracy:.2f}%"
        )

    def reset_test(self):
        """Reset the typing test."""
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(1.0, tk.END)
        self.start_time = None
        self.end_time = None
        self.highlight_text()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()