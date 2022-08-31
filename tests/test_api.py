from app import app


def test_api_posts():
    response = app.test_client().get('/api/posts/')
    assert type(response.json) == list, 'Значение не список'
    assert response.json[0]['pk'] == 1, 'Неправильные данные'

def test_api_posts_postid():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict, 'Значение не список'
    assert response.json['pk'] == 1, 'Неправильные данные'
