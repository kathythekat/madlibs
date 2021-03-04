from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

stories = [silly_story, excited_story]
story = []


@app.route('/')
def index():
    t1 = silly_story.name
    t2 = excited_story.name
    return render_template('home.html', t1=t1, t2=t2)


@app.route('/questions')
def form():
    story_name = request.args['story']
    for s in stories:
        if s.name.startswith(story_name):
            story.append(s)
    lst_words = story[0].prompts
    return render_template("questions.html", lst_words=lst_words)


@app.route('/story')
def get_story():
    text = story[0].generate(dict(request.args))
    return render_template('story.html', text=text)