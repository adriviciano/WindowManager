import json
import os


class ScreenConfig:
    CONFIG_FILE = "src/config/settings.json"

    def __init__(self):
        """
        Inicializa la configuración de la pantalla.
        Carga las configuraciones desde el archivo o establece valores predeterminados.
        """
        self.config = {
            "rows": 2,
            "cols": 2
        }
        self.load_config()

    def load_config(self):
        """
        Carga las configuraciones desde un archivo JSON.
        Si el archivo no existe, utiliza la configuración predeterminada.
        """
        if os.path.exists(self.CONFIG_FILE):
            try:
                with open(self.CONFIG_FILE, "r") as file:
                    self.config = json.load(file)
            except json.JSONDecodeError:
                print("Error al leer el archivo de configuración. Se utilizará la configuración predeterminada.")
        else:
            self.save_config()

    def save_config(self):
        """
        Guarda las configuraciones actuales en un archivo JSON.
        """
        with open(self.CONFIG_FILE, "w") as file:
            json.dump(self.config, file, indent=4)

    def set_config(self, rows, cols):
        """
        Establece una nueva configuración de filas y columnas.
        
        :param rows: Número de filas en la pantalla virtual.
        :param cols: Número de columnas en la pantalla virtual.
        """
        self.config["rows"] = rows
        self.config["cols"] = cols
        self.save_config()

    def get_config(self):
        """
        Obtiene la configuración actual de la pantalla.
        
        :return: Un diccionario con el número de filas y columnas.
        """
        return self.config


if __name__ == "__main__":
    # Ejemplo de uso
    config = ScreenConfig()

    print("Configuración actual:", config.get_config())

    # Cambiar configuración
    config.set_config(3, 3)
    print("Nueva configuración:", config.get_config())
