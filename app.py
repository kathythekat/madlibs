from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def form():
    lst_words = silly_story.prompts
    return render_template(
        'questions.html',
        lst_words = lst_words
    )

@app.route('/story')
def get_story():
    text = silly_story.generate(dict(request.args))
    return render_template(
        'story.html',
        text = text
    )