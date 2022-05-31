import logging

from flask import Blueprint, render_template, request, current_app

from classes.data_class import Data
from classes.exceptions import DataSourceBrokenException

# Создаем блупринт, выбираем для него имя
main_blueprint = Blueprint('main_blueprint', __name__)

# Добавляем логгер
logger = logging.getLogger("basic")

@main_blueprint.route("/")
def main_page():
    """ Это вьюшка для главной страницы"""
    return render_template("index.html")


@main_blueprint.route("/search/")
def search_page():
    """Это вьюшка для страницы поиска"""

    path = current_app.config.get("POST_PATH")
    data = Data(path)

    s = request.args.get('s', "")

    # Логер, фиксирующий поиск
    logger.info(f"Выполняется поиск {s}")

    posts = data.search(s)

    return render_template("post_list.html", posts=posts, s=s)


@main_blueprint.errorhandler(DataSourceBrokenException)
def data_source_broken_error(e):
    return f"Файл с данными поврежден"

