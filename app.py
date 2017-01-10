from flask import Flask, request, render_template
from controllers.movie_controller import MovieController

movie_controller = MovieController()

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', movies=movie_controller.render_movies())

if __name__ == '__main__':
    app.run()
