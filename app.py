from flask import Flask

from posts.views import post_blueprint

app = Flask(__name__)
app.register_blueprint(post_blueprint)

@app.errorhandler(404)
def page_error_1(error):
    return 'Ой, какая-то ошибка в запросе', 404

@app.errorhandler(500)
def page_error_2(error):
    return 'Что-то сломалось на сервере', 500



if __name__ == '__main__':
    app.run()
