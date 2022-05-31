# Класс данных

import json

from classes.exceptions import DataSourceBrokenException


class Data:

    def __init__(self, path):
        self.path = path

    def _load_data_from_json(self):
        """
        Загружает данные из json
        """
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataSourceBrokenException("Файл с данными поврежден")
        return data

    def _save_data(self, data):
        """
        Открывает файл для записи
        """
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def search(self, substring):
        """
        Возвращает посты по вхождению строки
        """
        posts = self._load_data_from_json()
        posts_found = []

        for post in posts:
            if substring.lower() in post["content"].lower():
                posts_found.append(post)

        return posts_found

    def add_post(self, post):
        """
        Сохраняет пост
        """
        posts = self._load_data_from_json()
        posts.append(post)
        self._save_data(posts)

