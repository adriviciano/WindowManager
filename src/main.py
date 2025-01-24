from ui.main_window import MainWindow
import sys

def main():
    """
    Punto de entrada principal para la aplicación.
    Inicializa la interfaz gráfica y configura los módulos necesarios.
    """
    try:
        # Inicializar la ventana principal
        app = MainWindow()
        app.run()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
