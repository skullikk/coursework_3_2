import json


class PostsDAO:

    def load_posts(self):
        """Загружает посты из json файла"""
        with open('./data/posts.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_all(self) -> list[dict]:
        """Возвращает список постов"""
        return self.load_posts()

    def get_by_user(self, username: str) -> list[dict]:
        """Возвращает список постов по пользователю или ошибку, если пользователя нет"""
        result_by_user = []
        result_name = []
        for post in self.load_posts():
            result_name.append(post['poster_name'])
            if post['poster_name'] == username:
                result_by_user.append(post)
        if username not in result_name:
            raise ValueError('Нет такого пользователя')
        return result_by_user

    def search_for_posts(self, query: str) -> list[dict]:
        """Возвращает список постов по искомому слову"""
        result_search = []
        for post in self.load_posts():
            if query.lower() in post['content'].lower():
                result_search.append(post)
        return result_search

    def get_by_pk(self, pk: int) -> dict:
        """Возвращает пост по pk или ошибку, если поста нет"""
        result_post_id = []
        for post in self.load_posts():
            result_post_id.append(post['pk'])
            if post['pk'] == pk:
                return post
        if pk not in result_post_id:
            raise ValueError('Нет такого поста')
