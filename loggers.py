import logging


def create_logger():
    # Cоздаем певый логер уровня DEBUG
    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    # Cоздаем второй логер уровня DEBUG
    logger_two = logging.getLogger("ERROR")
    logger_two.setLevel("ERROR")

    # Настраиваем обработчики для логеров
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("logs/basic.txt")

    console_handler_two = logging.StreamHandler()
    file_handler_two = logging.FileHandler("logs/errors.txt")

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger_two.addHandler(console_handler_two)
    logger_two.addHandler(file_handler_two)

    # Добавляем форматтеры 1

    formatter_one = logging.Formatter("%(asctime)s : %(message)s")

    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)

    # Добавляем форматтеры 2

    formatter_two = logging.Formatter("%(asctime)s : %(message)s")

    console_handler_two.setFormatter(formatter_two)
    file_handler_two.setFormatter(formatter_two)

