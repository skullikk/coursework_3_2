import json

class CommetsDAO:

    def load_comments(self):
        with open('./data/comments.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_by_post_id(self, id):
        result_comments = []
        result_post_id = []
        for comment in self.load_comments():
            result_post_id.append(comment['post_id'])
            if comment['post_id'] == id:
                result_comments.append(comment)
        if id not in result_post_id:
            raise ValueError('Нет такого поста')
        return result_comments