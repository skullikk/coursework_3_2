import pytest

from posts.dao.posts_dao import PostsDAO

test_post_dao = PostsDAO()

def test_get_all():
    assert test_post_dao.get_all()[0]['poster_name'] == 'leo', 'Ошибка получения всех пользователей'

def test_get_by_user():
    assert test_post_dao.get_by_user('leo')[0]['pk'] == 1, 'Ошибка получения постов по пользователю'

def test_get_by_user_wrong():
    with pytest.raises(ValueError):
        test_post_dao.get_by_user('givi')

def test_search_by_post():
    assert test_post_dao.search_for_posts('катер')[0]['pk'] == 8, 'Ошибка поиска поста'

def test_get_by_pk():
    assert test_post_dao.get_by_pk(8)['poster_name'] == 'larry', 'Ошибка поиска поста по id'

def test_get_by_pk_wrong():
    with pytest.raises(ValueError):
        test_post_dao.get_by_pk(9)