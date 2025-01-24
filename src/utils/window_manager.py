import win32gui
import win32con
import win32api
from config.screen_config import ScreenConfig
import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, messagebox, Listbox, MULTIPLE


class WindowManager:
    def __init__(self):
        """
        Inicializa el gestor de ventanas y obtiene las dimensiones de la pantalla.
        """
        self.screen_width = win32api.GetSystemMetrics(0)
        self.screen_height = win32api.GetSystemMetrics(1) - win32api.GetSystemMetrics(4)  # Exclude taskbar height
        self.config = ScreenConfig()  # Carga la configuración actual

    @staticmethod
    def list_windows():
        """
        Lista las ventanas visibles con títulos válidos y las filtra para excluir ventanas irrelevantes.
        
        :return: Una lista de tuplas (hwnd, título).
        """
        windows = []

        def enum_window_callback(hwnd, _):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                # Excluir ventanas sin título o del sistema
                if title and title.strip() and "Program Manager" not in title:
                    windows.append((hwnd, title))

        win32gui.EnumWindows(enum_window_callback, None)
        return windows

    def move_window_to_region(self, hwnd, region):
        """
        Mueve una ventana a una región específica.
        
        :param hwnd: Handle de la ventana.
        :param region: Región de la pantalla (x, y, width, height).
        """
        x, y, width, height = region
        win32gui.MoveWindow(hwnd, x, y, width, height, True)

    def arrange_selected_windows(self, selected_windows):
        """
        Asigna ventanas seleccionadas a regiones virtuales automáticamente.
        """
        count = len(selected_windows)
        if count == 1:
            self.move_window_to_region(selected_windows[0][0], (0, 0, self.screen_width, self.screen_height))
        elif count == 2:
            width = self.screen_width // 2
            band_height = self.screen_height // 4  # Altura de las bandas negras (ajusta según preferencia)
            height = self.screen_height // 2
            regions = [(0, band_height, width, height), (width, band_height, width, height)]
        elif count == 4:
            width = self.screen_width // 2
            height = self.screen_height // 2
            regions = [
                (0, 0, width, height),
                (width, 0, width, height),
                (0, height, width, height),
                (width, height, width, height)
            ]
        else:
            messagebox.showerror("Error", "Unsupported number of windows selected.")
            return

        for i, (hwnd, title) in enumerate(selected_windows):
            self.move_window_to_region(hwnd, regions[i % len(regions)])
            print(f"Window '{title}' moved to region {regions[i % len(regions)]}")
