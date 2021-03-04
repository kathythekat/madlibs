from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

stories = [silly_story, excited_story]
story = None

@app.route('/')
def index():
    t1 = silly_story.name
    t2 = excited_story.name
    return render_template('home.html', t1=t1 , t2=t2)

@app.route('/questions')
def form():
    story_name = request.args['story']
    for s in stories:
        if s.name.startswith(story_name):
            story = s
            print("made it")
    lst_words = story.prompts
    return render_template("questions.html", lst_words = lst_words)

@app.route('/story')
def get_story():
    print(story)
    text = story.generate(dict(request.args))
    return render_template('story.html', text = text)