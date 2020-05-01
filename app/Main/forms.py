from flask_wtf import FlaskForm
#Imported classes facilitate the creation of input and textare fields and submit button
from flask_wtf.file import FileField,FileAllowed,FileRequired
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
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):

    '''
    Class facilitates the creation of profile objects
    '''
    bio = TextAreaField('So tell us everything...',validators = [Required()])
    submit = SubmitField('Add Bio')

class UploadFile(FlaskForm):

    photo = FileField(validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'])])
