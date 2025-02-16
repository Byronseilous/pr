import tkinter as tk
from tkinter import messagebox, ttk
import time
import json
import os
from tkinter import PhotoImage

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

        # File to store user data
        self.USER_DATA_FILE = "user_data.json"

        # Load existing user data or initialize an empty dictionary
        self.users = self.load_user_data()

        # Load icons
        self.load_icons()

        # Show the login screen initially
        self.show_login_screen()

    def load_icons(self):
        """Load icons for the UI."""
        try:
            self.login_icon = PhotoImage(file="login_icon.png").subsample(2, 2)
            self.create_account_icon = PhotoImage(file="create_account_icon.png").subsample(2, 2)
            self.start_icon = PhotoImage(file="start_icon.png").subsample(2, 2)
            self.reset_icon = PhotoImage(file="reset_icon.png").subsample(2, 2)
        except Exception as e:
            print("Icons not found. Using text-only buttons.")
            self.login_icon = None
            self.create_account_icon = None
            self.start_icon = None
            self.reset_icon = None

    def show_login_screen(self):
        """Display the login screen."""
        self.clear_screen()

        # Create a frame to center the content
        center_frame = tk.Frame(self.root, bg=self.COLORS["background"])
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Login screen widgets
        self.login_label = tk.Label(
            center_frame, text="Login or Create Account", font=("Helvetica", 24, "bold"),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.login_label.pack(pady=20)

        # Username entry
        self.username_label = tk.Label(
            center_frame, text="Username:", font=("Helvetica", 16),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(
            center_frame, font=("Helvetica", 16), bg=self.COLORS["background"], fg=self.COLORS["text"]
        )
        self.username_entry.pack(pady=5)

        # Password entry
        self.password_label = tk.Label(
            center_frame, text="Password:", font=("Helvetica", 16),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(
            center_frame, font=("Helvetica", 16), bg=self.COLORS["background"], fg=self.COLORS["text"], show="*"
        )
        self.password_entry.pack(pady=5)

        # Login button
        self.login_button = tk.Button(
            center_frame, text="Login", command=self.login, font=("Helvetica", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat"
        )
        if self.login_icon:
            self.login_button.config(image=self.login_icon, compound="left")
        self.login_button.pack(pady=10)

        # Create account button
        self.create_account_button = tk.Button(
            center_frame, text="Create Account", command=self.show_create_account_screen, font=("Helvetica", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat"
        )
        if self.create_account_icon:
            self.create_account_button.config(image=self.create_account_icon, compound="left")
        self.create_account_button.pack(pady=10)

    def load_user_data(self):
        """Load user data from a JSON file."""
        if os.path.exists(self.USER_DATA_FILE):
            with open(self.USER_DATA_FILE, "r") as file:
                return json.load(file)
        return {}

    def save_user_data(self):
        """Save user data to a JSON file."""
        with open(self.USER_DATA_FILE, "w") as file:
            json.dump(self.users, file)

    def show_login_screen(self):
        """Display the login screen."""
        self.clear_screen()

        # Create a frame to center the content
        center_frame = tk.Frame(self.root, bg=self.COLORS["background"])
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Login screen widgets
        self.login_label = tk.Label(
            center_frame, text="Login or Create Account", font=("Helvetica", 24, "bold"),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.login_label.pack(pady=20)

        # Username entry
        self.username_label = tk.Label(
            center_frame, text="Username:", font=("Helvetica", 16),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(
            center_frame, font=("Helvetica", 16), bg=self.COLORS["background"], fg=self.COLORS["text"]
        )
        self.username_entry.pack(pady=5)

        # Password entry
        self.password_label = tk.Label(
            center_frame, text="Password:", font=("Helvetica", 16),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(
            center_frame, font=("Helvetica", 16), bg=self.COLORS["background"], fg=self.COLORS["text"], show="*"
        )
        self.password_entry.pack(pady=5)

        # Login button
        self.login_button = tk.Button(
            center_frame, text="Login", command=self.login, font=("Helvetica", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat", image=self.login_icon, compound="left"
        )
        self.login_button.pack(pady=10)

        # Create account button
        self.create_account_button = tk.Button(
            center_frame, text="Create Account", command=self.show_create_account_screen, font=("Helvetica", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat", image=self.create_account_icon, compound="left"
        )
        self.create_account_button.pack(pady=10)

    def show_create_account_screen(self):
        """Display the create account screen."""
        self.clear_screen()

        # Create a frame to center the content
        center_frame = tk.Frame(self.root, bg=self.COLORS["background"])
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create account screen widgets
        self.create_account_label = tk.Label(
            center_frame, text="Create Account", font=("Helvetica", 24, "bold"),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.create_account_label.pack(pady=20)

        # Username entry
        self.new_username_label = tk.Label(
            center_frame, text="Username:", font=("Helvetica", 16),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.new_username_label.pack(pady=5)
        self.new_username_entry = tk.Entry(
            center_frame, font=("Helvetica", 16), bg=self.COLORS["background"], fg=self.COLORS["text"]
        )
        self.new_username_entry.pack(pady=5)

        # Password entry
        self.new_password_label = tk.Label(
            center_frame, text="Password:", font=("Helvetica", 16),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.new_password_label.pack(pady=5)
        self.new_password_entry = tk.Entry(
            center_frame, font=("Helvetica", 16), bg=self.COLORS["background"], fg=self.COLORS["text"], show="*"
        )
        self.new_password_entry.pack(pady=5)

        # Confirm password entry
        self.confirm_password_label = tk.Label(
            center_frame, text="Confirm Password:", font=("Helvetica", 16),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.confirm_password_label.pack(pady=5)
        self.confirm_password_entry = tk.Entry(
            center_frame, font=("Helvetica", 16), bg=self.COLORS["background"], fg=self.COLORS["text"], show="*"
        )
        self.confirm_password_entry.pack(pady=5)

        # Create account button
        self.create_account_final_button = tk.Button(
            center_frame, text="Create Account", command=self.create_account, font=("Helvetica", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat", image=self.create_account_icon, compound="left"
        )
        self.create_account_final_button.pack(pady=10)

        # Back to login button
        self.back_to_login_button = tk.Button(
            center_frame, text="Back to Login", command=self.show_login_screen, font=("Helvetica", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat"
        )
        self.back_to_login_button.pack(pady=10)

    def create_account(self):
        """Create a new account."""
        username = self.new_username_entry.get().strip()
        password = self.new_password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()

        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        if username in self.users:
            messagebox.showerror("Error", "Username already exists!")
            return

        # Store the new user
        self.users[username] = password
        self.save_user_data()  # Save user data to file
        messagebox.showinfo("Success", "Account created successfully!")
        self.show_login_screen()

    def login(self):
        """Log in the user."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required!")
            return

        if username not in self.users or self.users[username] != password:
            messagebox.showerror("Error", "Invalid username or password!")
            return

        # Successful login
        self.current_user = username
        self.show_welcome_screen()

    def show_welcome_screen(self):
        """Display the welcome screen with the username."""
        self.clear_screen()

        # Create a frame to center the content
        center_frame = tk.Frame(self.root, bg=self.COLORS["background"])
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.welcome_label = tk.Label(
            center_frame, text=f"Welcome, {self.current_user}!", font=("Helvetica", 24, "bold"),
            fg=self.COLORS["text"], bg=self.COLORS["background"]
        )
        self.welcome_label.pack(pady=50)

        # Start button
        self.start_button = tk.Button(
            center_frame, text="Start Typing Test", command=self.start_test, font=("Helvetica", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat", image=self.start_icon, compound="left"
        )
        self.start_button.pack(pady=20)

    def clear_screen(self):
        """Clear all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_test(self):
        """Start the typing test."""
        self.clear_screen()

        # Create a frame to center the content
        center_frame = tk.Frame(self.root, bg=self.COLORS["background"])
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Sample text and typing area
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.sample_display = tk.Text(
            center_frame, height=5, width=60, font=("Courier New", 16), wrap="word", state=tk.DISABLED,
            bg=self.COLORS["background"], fg=self.COLORS["text"]
        )
        self.entry = tk.Text(
            center_frame, height=10, width=60, font=("Courier New", 16),
            bg=self.COLORS["background"], fg=self.COLORS["text"], insertbackground=self.COLORS["text"]
        )
        self.reset_button = tk.Button(
            center_frame, text="Reset", command=self.reset_test, font=("Helvetica", 16),
            bg=self.COLORS["button"], fg=self.COLORS["text"], relief="flat", image=self.reset_icon, compound="left"
        )

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