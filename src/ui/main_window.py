import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, messagebox
from src.utils.window_manager import WindowManager
from src.config.screen_config import ScreenConfig
class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Screen Manager")
        self.root.geometry("800x600")
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        config_menu = tk.Menu(menu_bar, tearoff=0)
        config_menu.add_command(label="Configurar Pantallas", command=self.configure_screens)
        config_menu.add_separator()
        config_menu.add_command(label="Salir", command=self.root.quit)
        menu_bar.add_cascade(label="Opciones", menu=config_menu)
        self.root.config(menu=menu_bar)

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Administrador de Pantallas Virtuales", font=("Arial", 16))
        title_label.pack(pady=20)
        configure_button = tk.Button(self.root, text="Configurar Pantallas", command=self.configure_screens)
        configure_button.pack(pady=10)
        close_button = tk.Button(self.root, text="Salir", command=self.root.quit)
        close_button.pack(pady=10)

    def configure_screens(self):
        messagebox.showinfo("Configurar Pantallas", "Función en desarrollo.")

    def run(self):
        self.root.mainloop()

    def configure_screens(self):
        """
        Abre una ventana para configurar las divisiones de pantalla.
        """
        config_window = Toplevel(self.root)
        config_window.title("Configurar Pantallas")
        config_window.geometry("300x200")

        screen_config = ScreenConfig()
        manager = WindowManager()

        current_config = screen_config.get_config()
        rows_var = tk.StringVar(value=current_config["rows"])
        cols_var = tk.StringVar(value=current_config["cols"])

        Label(config_window, text="Número de filas:").pack(pady=5)
        rows_entry = Entry(config_window, textvariable=rows_var)
        rows_entry.pack(pady=5)

        Label(config_window, text="Número de columnas:").pack(pady=5)
        cols_entry = Entry(config_window, textvariable=cols_var)
        cols_entry.pack(pady=5)

        def save_and_apply_config():
            """
            Guarda la configuración y aplica las divisiones.
            """
            try:
                rows = int(rows_var.get())
                cols = int(cols_var.get())

                if rows <= 0 or cols <= 0:
                    raise ValueError("Las filas y columnas deben ser mayores a 0.")

                screen_config.set_config(rows, cols)
                manager.assign_windows_to_regions()  # Aplica las divisiones
                config_window.destroy()
                messagebox.showinfo("Éxito", "La configuración ha sido guardada y aplicada.")
            except ValueError as e:
                messagebox.showerror("Error", f"Configuración inválida: {e}")

        Button(config_window, text="Guardar y Aplicar", command=save_and_apply_config).pack(pady=20)
