from flask import Flask

from posts.views import post_blueprint

app = Flask(__name__)
app.register_blueprint(post_blueprint)

@app.errorhandler(404)
def page_error(error):
    return 'Ой, какая то ошибка'


if __name__ == '__main__':
    app.run()
