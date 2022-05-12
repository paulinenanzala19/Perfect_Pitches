from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch,User,Comments,Upvote,Downvote
from .forms import PitchForm,UpdateProfile,CommentForm
from flask_login import login_required,current_user
from .. import db,photos

@main.route('/')
def index():

    title='Perfect Pitch'

    pitches = Pitch.query.all()
    pickuplines = Pitch.query.filter_by(category = 'pickuplines').all() 
    idea = Pitch.query.filter_by(category = 'idea').all()
    music = Pitch.query.filter_by(category = 'music').all()
    business=Pitch.query.filter_by(category='business').all()
    return render_template('index.html',title=title,pickuplines=pickuplines,idea=idea,music=music,business=business)
    

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

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
  comments = Comments.query.filter_by(pitch_id=pitch_id).all()
  form = CommentForm()
  if form.validate_on_submit():
    comment = form.comment.data

    new_comment_obj = Comments(comment=comment, pitch_id=pitch_id, user_id = current_user._get_current_object().id)

    new_comment_obj.save_comment()
    return redirect(url_for('main.comment', pitch_id=pitch_id))

  return render_template('comment.html', form=form, comments=comments)

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def likes(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save_upvote()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislikes(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save_downvote()
    return redirect(url_for('main.index',id = id))