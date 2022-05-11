from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[InputRequired()])
    post = TextAreaField('Pitch content', validators=[InputRequired()])
    # text = TextAreaField('Pitch content', validators=[InputRequired()])
    category=SelectField('Type', choices=[('business','business_pitches'),('pickuplines','pickup-lines_pitches'),('idea','idea_pitches'),('music','music_pitches')],validators=[InputRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add a little spice to your profile.',validators = [InputRequired()])
    submit = SubmitField('Submit')