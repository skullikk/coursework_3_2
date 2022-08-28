from flask import Blueprint, render_template
from .dao.posts_dao import PostsDAO

post_blueprint = Blueprint('posts_blueprint', __name__)
posts_dao = PostsDAO()

@post_blueprint.route('/')
def page_post_all():
    posts = posts_dao.get_all()
    return render_template('index.html', posts=posts)

@post_blueprint.route('/post/<int:post_id>')
def page_post(post_id):
    post = posts_dao.get_by_pk(post_id)
    return render_template('post.html', post=post)

