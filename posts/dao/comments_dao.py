import json

class CommentsDAO:

    def load_comments(self):
        with open('./data/comments.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_by_post_id(self, id):
        result_comments = []
        for comment in self.load_comments():
            if comment['post_id'] == id:
                result_comments.append(comment)
        return result_comments