from flask import Blueprint, render_template, request

from .dao.comments_dao import CommentsDAO
from .dao.posts_dao import PostsDAO

post_blueprint = Blueprint('posts_blueprint', __name__)
posts_dao = PostsDAO()
comments_dao = CommentsDAO()

@post_blueprint.route('/')
def page_post_all():
    posts = posts_dao.get_all()
    return render_template('index.html', posts=posts)

@post_blueprint.route('/post/<int:postid>')
def page_post(postid):
    post = posts_dao.get_by_pk(postid)
    comments = comments_dao.get_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments)

@post_blueprint.route('/search/')
def page_search():
    s = request.args.get('s')
    search_posts = posts_dao.search_for_posts(s)
    return render_template('search.html', posts=search_posts)

@post_blueprint.route('/users/<username>')
def page_user(username):
    posts = posts_dao.get_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)

