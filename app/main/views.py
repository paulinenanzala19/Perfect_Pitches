from flask import render_template
from . import main
from ..models import Pitch

@main.route('/')
def index():

    pickuplines_pitches=Pitch.get_pitches('pickuplines')
    idea_pitches=Pitch.get_pitches('idea')
    music_pitches=Pitch.get_pitches('music')
    business_pitches=Pitch.get_pitches('business')


    return render_template('index.html',pickuplines=pickuplines_pitches, 
    idea=idea_pitches,music=music_pitches,business=business_pitches)

@main.route('/pitches/business_pitches')
def business_pitches():

    pitches = Pitch.get_pitches('business')

    return render_template("business_pitches.html", pitches = pitches)
    
