import win32gui
import win32con
import win32api
from src.config.screen_config import ScreenConfig


class WindowManager:
    def __init__(self):
        """
        Inicializa el gestor de ventanas y obtiene las dimensiones de la pantalla.
        """
        self.screen_width = win32api.GetSystemMetrics(0)
        self.screen_height = win32api.GetSystemMetrics(1)
        self.config = ScreenConfig()  # Carga la configuración actual

    def divide_screen(self):
        """
        Divide la pantalla principal en regiones según la configuración del JSON.
        
        :return: Lista de regiones de pantalla como (x, y, width, height).
        """
        config = self.config.get_config()
        rows, cols = config["rows"], config["cols"]

        regions = []
        cell_width = self.screen_width // cols
        cell_height = self.screen_height // rows

        for row in range(rows):
            for col in range(cols):
                x = col * cell_width
                y = row * cell_height
                regions.append((x, y, cell_width, cell_height))

        return regions

    def list_windows(self):
        """
        Lista todas las ventanas abiertas en el sistema.
        """
        def enum_windows_callback(hwnd, windows):
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
                windows.append((hwnd, win32gui.GetWindowText(hwnd)))
            return True

        windows = []
        win32gui.EnumWindows(enum_windows_callback, windows)
        return windows

    def move_window_to_region(self, hwnd, region):
        """
        Mueve una ventana a una región específica.
        
        :param hwnd: Handle de la ventana.
        :param region: Región de la pantalla (x, y, width, height).
        """
        x, y, width, height = region
        win32gui.MoveWindow(hwnd, x, y, width, height, True)

    def assign_windows_to_regions(self):
        """
        Asigna ventanas abiertas a regiones virtuales automáticamente.
        """
        regions = self.divide_screen()
        windows = self.list_windows()

        if not regions or not windows:
            print("No hay ventanas abiertas o regiones configuradas.")
            return

        for i, (hwnd, title) in enumerate(windows):
            region = regions[i % len(regions)]  # Asignar ventanas en bucle a las regiones
            self.move_window_to_region(hwnd, region)
            print(f"Ventana '{title}' movida a región {region}")


if __name__ == "__main__":
    manager = WindowManager()

    print("Dividiendo pantalla...")
    regions = manager.divide_screen()
    print("Regiones:", regions)

    print("\nAsignando ventanas a regiones...")
    manager.assign_windows_to_regions()
