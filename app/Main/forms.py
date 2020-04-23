from flask_wtf import FlaskForm
#Imported classes facilitate the creation of input and textare fields and submit button
from wtforms import StringField, TextAreaField, SubmitField
#Imported class facilitates form validation
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    '''
    Class inherits from the FlaskForm class and facilitates the creation of review form objects

    Args:
        title (str): StringField
        review (str): TextAreaField
        submit: SubmitField
    '''
    title = StringField('Review title', validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')
