import pytest

from posts.dao.posts_dao import PostsDAO

test_post_dao = PostsDAO()

def test_get_all():
    assert test_post_dao.get_all()[0]['poster_name'] == 'leo', 'Ошибка получения всех пользователей'