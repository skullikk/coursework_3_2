from flask import Flask, jsonify
import logging

from posts.dao.posts_dao import PostsDAO
from posts.views import post_blueprint

app = Flask(__name__)
app.register_blueprint(post_blueprint)
app.json.ensure_ascii = False

logger = logging.getLogger('api_logger')
logger.setLevel('INFO')
f_handler = logging.FileHandler('./logs/api.log', mode='a')
logger.addHandler(f_handler)
f = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
f_handler.setFormatter(f)


@app.route('/api/posts/')
def page_posts_json():
    logger.info('Запрос /api/posts/')
    posts = PostsDAO()
    return jsonify(posts.get_all())


@app.get('/api/posts/<int:post_id>')
def page_post_id(post_id):
    logger.info(f'Запрос /api/posts/{post_id}')
    posts = PostsDAO()
    return jsonify(posts.get_by_pk(post_id))


@app.errorhandler(404)
def page_error_1(error):
    page_404 = '''<h1>Ой, ну все. Вы не туда пошли...</h1>
              <p><a href="/">Back</a></p>'''
    return page_404, 404


@app.errorhandler(500)
def page_error_2(error):
    page_500 = '''<h1>Админ знает, админ не спит</h1>
                  <p>Скоро все поправит!</p>
                  <p><a href="/">Back</a></p>'''
    return page_500, 500


if __name__ == '__main__':
    app.run()
