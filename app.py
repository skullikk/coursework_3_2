from flask import Flask, jsonify


from posts.views import post_blueprint

app = Flask(__name__)
app.register_blueprint(post_blueprint)


@app.route('/api/posts/')
def page_posts_json():
    pass

@app.errorhandler(404)
def page_error_1(error):
    page_404 = '''<h1>File Not Found</h1>
              <p><a href="/">Back</a></p>'''
    return page_404

@app.errorhandler(500)
def page_error_2(error):
    page_500 = '''<h1>An unexpected error has occurred</h1>
                  <p>The administrator has been notified. Sorry for the inconvenience!</p>
                  <p><a href="/">Back</a></p>'''
    return page_500


if __name__ == '__main__':
    app.run()

