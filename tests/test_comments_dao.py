import pytest

from posts.dao.comments_dao import CommentsDAO

test_comments_dao = CommentsDAO()

def test_get_by_post_id():
    assert test_comments_dao.get_by_post_id(1)[0]['commenter_name'] == 'hanna', 'Ошибка выбора комментария по id поста'
