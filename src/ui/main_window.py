import tkinter as tk
from tkinter import Toplevel, Label, Button, messagebox, Listbox, MULTIPLE
from utils.window_manager import WindowManager

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Window Manager")
        self.root.geometry("800x600")
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        config_menu = tk.Menu(menu_bar, tearoff=0)
        config_menu.add_command(label="Manage Windows", command=self.configure_screens)
        config_menu.add_separator()
        config_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="Options", menu=config_menu)
        self.root.config(menu=menu_bar)

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Window Manager", font=("Arial", 16))
        title_label.pack(pady=20)
        configure_button = tk.Button(self.root, text="Manage Windows", command=self.configure_screens)
        configure_button.pack(pady=10)
        close_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        close_button.pack(pady=10)

    def configure_screens(self):
        config_window = Toplevel(self.root)
        config_window.title("Manage Windows")
        config_window.geometry("400x400")

        manager = WindowManager()
        windows = manager.list_windows()

        Label(config_window, text="Select Windows to Arrange:").pack(pady=5)
        windows_listbox = Listbox(config_window, selectmode=MULTIPLE)
        for hwnd, title in windows:
            windows_listbox.insert(tk.END, title)
        windows_listbox.pack(pady=5, fill=tk.BOTH, expand=True)

        def apply_configuration():
            selected_indices = windows_listbox.curselection()
            selected_windows = [windows[i] for i in selected_indices]
            manager.arrange_selected_windows(selected_windows)
            config_window.destroy()
            messagebox.showinfo("Success", "Windows arranged successfully.")

        Button(config_window, text="Apply", command=apply_configuration).pack(pady=20)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.run()
