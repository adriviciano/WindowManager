import logging
import os


class Logger:
    def __init__(self, log_file="src/logs/app.log", log_level=logging.INFO):
        """
        Inicializa el sistema de logging.

        :param log_file: Ruta del archivo de log.
        :param log_level: Nivel de log (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        """
        # Crear directorio de logs si no existe
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Configuración básica del logger
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()  # Muestra logs en la consola
            ]
        )
        self.logger = logging.getLogger()

    def debug(self, message):
        """
        Registra un mensaje de nivel DEBUG.
        """
        self.logger.debug(message)

    def info(self, message):
        """
        Registra un mensaje de nivel INFO.
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Registra un mensaje de nivel WARNING.
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Registra un mensaje de nivel ERROR.
        """
        self.logger.error(message)

    def critical(self, message):
        """
        Registra un mensaje de nivel CRITICAL.
        """
        self.logger.critical(message)


if __name__ == "__main__":
    # Ejemplo de uso
    log = Logger(log_file="src/logs/example.log", log_level=logging.DEBUG)

    log.debug("Este es un mensaje de depuración.")
    log.info("Este es un mensaje informativo.")
    log.warning("Este es un mensaje de advertencia.")
    log.error("Este es un mensaje de error.")
    log.critical("Este es un mensaje crítico.")
