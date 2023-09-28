from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchWord(FlaskForm):
	word = StringField('Word:',render_kw={"placeholder": "Enter a word to look up..."}, validators=[DataRequired('Word Required')])
	submit = SubmitField('Get Definition')
