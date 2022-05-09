from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[InputRequired()])
    text = TextAreaField('Pitch review', validators=[InputRequired()])
    category=selectField('category' select=[('pickuplines','pickup-lines_pitches'),('idea','Idea_pitches'),('music','Music_pitches'),('business','Business_Pitches')])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')