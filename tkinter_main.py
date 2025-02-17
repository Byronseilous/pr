import tkinter as tk
from tkinter import messagebox, ttk
import time
import json
import os
from tkinter import PhotoImage

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test Pro")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen", False))


        self.COLORS = {
            "background": "#3B4252",
            "text": "#ECEFF4",
            "primary_button": "#8FBCBB",
            "secondary_button": "#5E81AC",
            "highlight": "#A3BE8C",
            "error": "#BF616A",
            "success": "#A3BE8C",
            "accent": "#D08770"
        }

        self.root.config(bg=self.COLORS["background"])

        self.USER_DATA_FILE = "user_data.json"
        self.users = self.load_user_data()
        self.load_icons()


        self.sample_texts = {
            "Beginner": "The quick brown fox jumps over the lazy dog.",
            "Intermediate": "Programming is a rewarding skill that allows you to create innovative solutions to complex problems.",
            "Advanced": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        }
        self.current_difficulty = "Beginner"

        self.configure_styles()
        self.show_login_screen()

    def load_icons(self):
        """Load icons for the UI."""
        try:
            icon_path = "icons"
            self.login_icon = PhotoImage(file=os.path.join(icon_path, "login_icon.png")).subsample(2, 2)
            self.create_account_icon = PhotoImage(file=os.path.join(icon_path, "create_account_icon.png")).subsample(2, 2)
            self.start_icon = PhotoImage(file=os.path.join(icon_path, "start_icon.png")).subsample(2, 2)
            self.reset_icon = PhotoImage(file=os.path.join(icon_path, "reset_icon.png")).subsample(2, 2)
        except Exception as e:
            print(f"Error loading icons: {e}. Using text-only buttons.")
            self.login_icon = None
            self.create_account_icon = None
            self.start_icon = None
            self.reset_icon = None

    def clear_screen(self):
        """Clear all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

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
        self.configure_styles()  #
        center_frame = ttk.Frame(self.root, padding="30 20", style="CenterFrame.TFrame")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(center_frame, text="Login", font=("Helvetica", 24, "bold"), style="TLabel").grid(column=0, row=0, pady=20, columnspan=2)

        ttk.Label(center_frame, text="Username:", font=("Helvetica", 14), style="TLabel").grid(column=0, row=1, sticky="w", pady=5)
        self.username_entry = ttk.Entry(center_frame, font=("Helvetica", 14), style="TEntry")
        self.username_entry.grid(column=1, row=1, sticky="ew", padx=10, pady=5)

        ttk.Label(center_frame, text="Password:", font=("Helvetica", 14), style="TLabel").grid(column=0, row=2, sticky="w", pady=5)
        self.password_entry = ttk.Entry(center_frame, font=("Helvetica", 14), show="*", style="TEntry")
        self.password_entry.grid(column=1, row=2, sticky="ew", padx=10, pady=5)

        login_button_text = "Login" if not self.login_icon else None
        create_account_button_text = "Create Account" if not self.create_account_icon else None

        login_button = ttk.Button(
            center_frame, text=login_button_text, command=self.login, style="PrimaryButton.TButton", image=self.login_icon, compound="left"
        )
        login_button.grid(column=0, row=3, columnspan=2, pady=15, sticky="ew")

        create_account_button = ttk.Button(
            center_frame, text=create_account_button_text, command=self.show_create_account_screen, style="SecondaryButton.TButton", image=self.create_account_icon, compound="left"
        )
        create_account_button.grid(column=0, row=4, columnspan=2, pady=5, sticky="ew")


        center_frame.columnconfigure(1, weight=1)


        self.configure_styles()

    def show_create_account_screen(self):
        """Display the create account screen."""
        self.clear_screen()

        center_frame = ttk.Frame(self.root, padding="30 20", style="CenterFrame.TFrame")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(center_frame, text="Create Account", font=("Helvetica", 24, "bold"), style="TLabel").grid(column=0, row=0, pady=20, columnspan=2)

        ttk.Label(center_frame, text="Username:", font=("Helvetica", 14), style="TLabel").grid(column=0, row=1, sticky="w", pady=5)
        self.new_username_entry = ttk.Entry(center_frame, font=("Helvetica", 14), style="TEntry")
        self.new_username_entry.grid(column=1, row=1, sticky="ew", padx=10, pady=5)

        ttk.Label(center_frame, text="Password:", font=("Helvetica", 14), style="TLabel").grid(column=0, row=2, sticky="w", pady=5)
        self.new_password_entry = ttk.Entry(center_frame, font=("Helvetica", 14), show="*", style="TEntry")
        self.new_password_entry.grid(column=1, row=2, sticky="ew", padx=10, pady=5)

        ttk.Label(center_frame, text="Confirm Password:", font=("Helvetica", 14), style="TLabel").grid(column=0, row=3, sticky="w", pady=5)
        self.confirm_password_entry = ttk.Entry(center_frame, font=("Helvetica", 14), show="*", style="TEntry")
        self.confirm_password_entry.grid(column=1, row=3, sticky="ew", padx=10, pady=5)

        create_account_button_text = "Create Account" if not self.create_account_icon else None

        create_account_final_button = ttk.Button(
            center_frame, text=create_account_button_text, command=self.create_account, style="PrimaryButton.TButton", image=self.create_account_icon, compound="left"
        )
        create_account_final_button.grid(column=0, row=4, columnspan=2, pady=15, sticky="ew")

        back_to_login_button = ttk.Button(
            center_frame, text="Back to Login", command=self.show_login_screen, style="SecondaryButton.TButton"
        )
        back_to_login_button.grid(column=0, row=5, columnspan=2, pady=5, sticky="ew")

        center_frame.columnconfigure(1, weight=1)
        self.configure_styles()

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

        self.users[username] = password
        self.save_user_data()
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

        self.current_user = username
        self.show_welcome_screen()

    def show_welcome_screen(self):
        """Display the welcome screen with the username and difficulty selection."""
        self.clear_screen()

        center_frame = ttk.Frame(self.root, padding="30 20", style="CenterFrame.TFrame")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(center_frame, text=f"Welcome, {self.current_user}!", font=("Helvetica", 24, "bold"), style="TLabel").grid(row=0, column=0, columnspan=2, pady=30)

        ttk.Label(center_frame, text="Select Difficulty:", font=("Helvetica", 14), style="TLabel").grid(row=1, column=0, sticky="w", pady=10)
        self.difficulty_var = tk.StringVar(value=self.current_difficulty)
        difficulty_combobox = ttk.Combobox(
            center_frame, textvariable=self.difficulty_var, values=list(self.sample_texts.keys()),
            state="readonly", font=("Helvetica", 14), style="TCombobox"
        )
        difficulty_combobox.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
        difficulty_combobox.bind("<<ComboboxSelected>>", self.update_difficulty)


        start_button_text = "Start Typing Test" if not self.start_icon else None
        start_button = ttk.Button(
            center_frame, text=start_button_text, command=self.start_test, style="PrimaryButton.TButton", image=self.start_icon, compound="left"
        )
        start_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew")

        center_frame.columnconfigure(1, weight=1)
        self.configure_styles()

    def update_difficulty(self, event):
        """Update the current difficulty based on combobox selection."""
        self.current_difficulty = self.difficulty_var.get()

    def start_test(self):
        """Start the typing test."""
        self.clear_screen()

        center_frame = ttk.Frame(self.root, padding="30 20", style="CenterFrame.TFrame")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.sample_text = self.sample_texts[self.current_difficulty]

        ttk.Label(center_frame, text=f"Difficulty: {self.current_difficulty}", font=("Helvetica", 14),
                  style="TLabel").grid(row=0, column=0, columnspan=2, pady=5)

        self.sample_display = tk.Text(
            center_frame, height=5, wrap="word", state=tk.DISABLED,
            font=("Courier New", 14), bd=0, highlightthickness=0,
            background=self.COLORS["background"],
            foreground=self.COLORS["text"]
        )
        self.sample_display.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        self.entry = tk.Text(
            center_frame, height=10, wrap="word",
            font=("Courier New", 14), bd=0, highlightthickness=0, insertbackground=self.COLORS["text"],
            background=self.COLORS["background"],
            foreground=self.COLORS["text"]
        )
        self.entry.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

        self.progress_bar = ttk.Progressbar(center_frame, orient=tk.HORIZONTAL, length=300, mode='determinate',
                                            style="TProgressbar")
        self.progress_bar.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        self.stats_frame = ttk.Frame(center_frame, style="CenterFrame.TFrame")
        self.stats_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        self.wpm_label = ttk.Label(self.stats_frame, text="WPM: 0", font=("Helvetica", 12),
                                   style="TLabel")
        self.wpm_label.grid(row=0, column=0, padx=20, sticky="w")
        self.accuracy_label = ttk.Label(self.stats_frame, text="Accuracy: 100.00%", font=("Helvetica", 12),
                                        style="TLabel")
        self.accuracy_label.grid(row=0, column=1, padx=20, sticky="e")
        self.stats_frame.columnconfigure(1, weight=1)

        reset_button_text = "Reset" if not self.reset_icon else None
        self.reset_button = ttk.Button(
            center_frame, text=reset_button_text, command=self.reset_test, style="SecondaryButton.TButton",
            image=self.reset_icon, compound="left"
        )
        self.reset_button.grid(row=5, column=0, columnspan=2, pady=15, sticky="ew")

        # Configure column weight for resizing
        center_frame.columnconfigure(0, weight=1)
        center_frame.columnconfigure(1, weight=1)

        self.sample_display.config(state=tk.NORMAL)
        self.sample_display.delete(1.0, tk.END)
        self.sample_display.insert(tk.END, self.sample_text)
        self.sample_display.config(state=tk.DISABLED)

        self.entry.config(state=tk.NORMAL)
        self.entry.delete(1.0, tk.END)
        self.entry.focus()

        self.start_time = time.time()
        self.entry.bind("<KeyRelease>", self.check_typing)
        self.update_stats_display(0, 100.00)

        self.configure_styles()

    def check_typing(self, event):
        """Check the user's typing, update UI and real-time stats."""
        typed_text = self.entry.get(1.0, tk.END).strip()
        self.highlight_text()
        accuracy = self.calculate_accuracy(typed_text)
        wpm = self.calculate_wpm(typed_text)
        self.update_stats_display(wpm, accuracy)
        self.update_progress_bar(len(typed_text), len(self.sample_text))

        if len(typed_text) >= len(self.sample_text):
            self.end_time = time.time()
            self.calculate_speed_and_accuracy(typed_text)
            self.entry.unbind("<KeyRelease>")

    def update_progress_bar(self, typed_length, total_length):
        """Update the progress bar."""
        if total_length > 0:
            progress_value = (typed_length / total_length) * 100
            self.progress_bar['value'] = progress_value
        else:
            self.progress_bar['value'] = 0

    def update_stats_display(self, wpm, accuracy):
        """Update the WPM and Accuracy labels in real-time."""
        self.wpm_label.config(text=f"WPM: {wpm:.0f}")
        self.accuracy_label.config(text=f"Accuracy: {accuracy:.2f}%")

    def highlight_text(self):
        """Highlight the sample text based on user input."""
        typed_text = self.entry.get(1.0, tk.END).strip()
        self.sample_display.config(state=tk.NORMAL)
        self.sample_display.delete(1.0, tk.END)

        for i in range(len(typed_text)):
            if i < len(self.sample_text):
                if typed_text[i] == self.sample_text[i]:
                    self.sample_display.insert(tk.END, self.sample_text[i], "correct")
                else:
                    self.sample_display.insert(tk.END, self.sample_text[i], "incorrect")
            else:
                self.sample_display.insert(tk.END, typed_text[i], "extra") # Highlight extra typed chars

        if len(typed_text) < len(self.sample_text):
            self.sample_display.insert(tk.END, self.sample_text[len(typed_text):])

        self.sample_display.config(state=tk.DISABLED)

        self.sample_display.tag_config("correct", foreground=self.COLORS["success"])
        self.sample_display.tag_config("incorrect", foreground=self.COLORS["error"])
        self.sample_display.tag_config("extra", foreground=self.COLORS["error"])

    def calculate_wpm(self, typed_text):
        """Calculate words per minute."""
        elapsed_time = time.time() - self.start_time
        if elapsed_time == 0:
            return 0
        words = len(typed_text.split()) / 5
        wpm = (words / elapsed_time) * 60
        return max(0, wpm)

    def calculate_accuracy(self, typed_text):
        """Calculate typing accuracy."""
        correct_chars = 0
        for i in range(min(len(typed_text), len(self.sample_text))):
            if typed_text[i] == self.sample_text[i]:
                correct_chars += 1
        total_chars = len(self.sample_text)
        if total_chars == 0:
            return 100.00
        accuracy = (correct_chars / total_chars) * 100
        return max(0.00, accuracy)

    def calculate_speed_and_accuracy(self, typed_text):
        """Final calculation and display of typing speed and accuracy after test completion."""
        time_taken = time.time() - self.start_time
        words = len(self.sample_text.split())
        wpm = (words / time_taken) * 60
        accuracy = self.calculate_accuracy(typed_text)

        messagebox.showinfo(
            "Typing Results",
            f"Your typing speed is: {wpm:.2f} WPM\n"
            f"Your accuracy is: {accuracy:.2f}%"
        )

    def reset_test(self):
        """Reset the typing test."""
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(1.0, tk.END)
        self.progress_bar['value'] = 0
        self.update_stats_display(0, 100.00)
        self.start_time = time.time()
        self.end_time = None
        self.highlight_text()
        self.entry.bind("<KeyRelease>", self.check_typing)

    def configure_styles(self):
        """Configure ttk styles for a modern look."""
        style = ttk.Style(self.root)


        style.configure("TLabel",
                        background=self.COLORS["background"],
                        foreground=self.COLORS["text"],
                        font=("Helvetica", 12))


        style.configure("TEntry",
                        background=self.COLORS["background"],
                        foreground=self.COLORS["text"],
                        insertcolor=self.COLORS["text"],
                        font=("Helvetica", 14))


        style.configure("TCombobox",
                        background=self.COLORS["background"],
                        foreground=self.COLORS["text"],
                        fieldbackground=self.COLORS["background"],
                        arrowcolor=self.COLORS["text"],
                        font=("Helvetica", 14))
        style.map("TCombobox",
                  background=[("active", self.COLORS["secondary_button"]), ("!disabled", self.COLORS["background"])],
                  foreground=[("!disabled", self.COLORS["text"])])


        style.configure("PrimaryButton.TButton",
                        background=self.COLORS["primary_button"],
                        foreground=self.COLORS["background"],
                        font=("Helvetica", 12, "bold"),
                        padding=10,
                        relief="flat",
                        borderwidth=0,
                        focuscolor=self.COLORS["accent"])
        style.map("PrimaryButton.TButton",
                  background=[("active", self.COLORS["highlight"]), ("!disabled", self.COLORS["primary_button"])],
                  foreground=[("active", self.COLORS["background"]), ("!disabled", self.COLORS["background"])])


        style.configure("SecondaryButton.TButton",
                        background=self.COLORS["secondary_button"],
                        foreground=self.COLORS["text"],
                        font=("Helvetica", 12),
                        padding=8,
                        relief="flat",
                        borderwidth=0,
                        focuscolor=self.COLORS["accent"])
        style.map("SecondaryButton.TButton",
                  background=[("active", self.COLORS["highlight"]), ("!disabled", self.COLORS["secondary_button"])],
                  foreground=[("active", self.COLORS["text"]), ("!disabled", self.COLORS["text"])])


        style.configure("CenterFrame.TFrame", background=self.COLORS["background"])


        style.configure("TProgressbar",
                        background=self.COLORS["primary_button"],
                        troughcolor=self.COLORS["background"],
                        borderwidth=0)
        style.layout("TProgressbar",
                     [('Horizontal.Progressbar.trough',
                       {'children': [('Horizontal.Progressbar.pbar',
                                      {'side': 'left', 'sticky': 'ns'})],
                        'sticky': 'nsew'})])

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()