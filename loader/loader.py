import os
import logging
from loader.utils import is_file_type_correct
from classes.data_class import Data
from flask import Blueprint, render_template, request, current_app

from loader.exceptions import PictureFormatNorSupportedError, PictureNotUploadedError

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")

# Добавляем логгеры
logger = logging.getLogger("basic")
logger_two = logging.getLogger("error")


@loader_blueprint.route("/post", methods=["GET"])
def page_post_form():
    """Вьюшка для формы загрузки поста"""
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    """ Эта вьюшка обрабатывает форму """
    picture = request.files.get("picture", None)
    content = request.values.get("content", "")

    # Обрабатываем картинку
    filename = picture.filename
    file_type = filename.split(".")[-1]

    # Проверяем, корректный ли формат

    if not is_file_type_correct(file_type):
        logger.info(f"Загруженный файл не поддерживается")
        raise PictureFormatNorSupportedError(f"Формат не поддерживается")

    # Сохраняем картинку
    os_path = os.path.join(".", "uploads", "images", filename)
    try:
        picture.save(os_path)
    except FileNotFoundError:
        logger_two.error(f"Ошибка при загрузке файла")
        raise PictureNotUploadedError(f"Ошибка при загрузке файла")

    web_path = f"/uploads/images/{filename}"
    pic = web_path

    post = {"pic": pic, "content": content}

    path = current_app.config.get("POST_PATH")
    data = Data(path)
    data.add_post(post)

    return render_template("post_uploaded.html", pic=pic, content=content)


@loader_blueprint.errorhandler(PictureFormatNorSupportedError)
def error_format_not_supported(e):
    return "Загруженный формат не поддерживается, выберите другой"


@loader_blueprint.errorhandler(PictureNotUploadedError)
def error_format_not_supported(e):
    return "Ошибка при загрузке файла. Перезагрузите страницу и попробуйте ещё"
