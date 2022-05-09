from flask import render_template
from . import main
from ..models import Pitch

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
def idea_pitches():
    pitches = Pitch.get_pitches('idea')
    return render_template("pickuplines_pitches.html", pitches = pitches)

@main.route('/pitches/music_pitches')
def idea_pitches():
    pitches = Pitch.get_pitches('idea')
    return render_template("music_pitches.html", pitches = pitches)
