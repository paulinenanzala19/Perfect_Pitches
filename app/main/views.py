from flask import render_template
from . import main
from ..models import Pitch
from .forms import PitchForm

@main.route('/')
def index():

    title='Perfect Pitch'

    pickuplines_pitches=Pitch.get_pitches('pickuplines')
    idea_pitches=Pitch.get_pitches('idea')
    music_pitches=Pitch.get_pitches('music')
    business_pitches=Pitch.get_pitches('business')


    return render_template('index.html',title=title,pickuplines=pickuplines_pitches, 
    idea=idea_pitches,music=music_pitches,business=business_pitches)

@main.route('/pitches/business_pitches')
def business_pitches():

    pitches = Pitch.get_pitches('business')

    return render_template("business_pitches.html", pitches = pitches)

@main.route('/pitches/idea_pitches')
def idea_pitches():
    pitches = Pitch.get_pitches('idea')
    return render_template("idea_pitches.html", pitches = pitches)
    
@main.route('/pitches/pickuplines_pitches')
def pickuplines_pitches():
    pitches = Pitch.get_pitches('idea')
    return render_template("pickuplines_pitches.html", pitches = pitches)

@main.route('/pitches/music_pitches')
def music_pitches():
    pitches = Pitch.get_pitches('idea')
    return render_template("music_pitches.html", pitches = pitches)
@main.route('/pitch/create', methods=['POST','GET'])
def create_pitch():
    form=PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        category = form.category.data
        
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_pitch()
        return redirect(url_for('main.index'))
        
    return render_template('create_pitches.html', form = form)