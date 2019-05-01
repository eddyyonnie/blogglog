from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField,TextAreaField
from wtforms.validators import ValidationError, DataRequired


class PostForm(FlaskForm):
    post = TextAreaField(('Say something'), validators=[DataRequired()])
    category = SelectField('Category', choices=[('Pickuplines','Pickuplines'),('Technology','Technology'),('Sales','Sales'),('Interview','Interview')])

    submit = SubmitField(('Submit'))

class CommentForm(FlaskForm):
    details = StringField('Write a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators = [Required()])
    submit = SubmitField('Submit')