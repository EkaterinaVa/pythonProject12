from flask import Flask, request, render_template, send_from_directory
from main.view import main_blueprint
from loader.loader import loader_blueprint
import logging
import loggers


app = Flask(__name__)

# Регистрируем блупринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config["POST_PATH"] = "posts.json"
app.config["UPLOAD_FOLDER"] = "uploads/images"

loggers.create_logger()

logger = logging.getLogger("basic")


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


logger.info("Приложение запущено")


if __name__ == "__main__":
    app.run(debug=True)

