from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch,User
from .forms import PitchForm,UpdateProfile
from flask_login import login_required,current_user
from .. import db,photos

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
@login_required
def create_pitch():
    form=PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id=current_user
        
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_pitch()
        return redirect(url_for('main.index'))
        
    return render_template('create_pitches.html', form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def upload_image(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
