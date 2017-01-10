from flask import Flask, request, render_template
from controllers.movie_controller import MovieController

controller = MovieController()

app = Flask(__name__)

@app.route('/')
def get_movies():
    return render_template('index.html', movies=controller.render_movies())

if __name__ == '__main__':
    app.run()
