
def is_file_type_correct(file_type):
    """Функция проверяет, подходит ли формат изображения"""
    if file_type.lower() in ["jpg", "jpeg", "gif"]:
        return True

